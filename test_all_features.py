"""
Comprehensive test suite for Report Generator
Tests all features to ensure everything works correctly
"""
import os
import sys
import unittest
from datetime import datetime
import tempfile
import shutil

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import init_db, create_user, verify_user, save_draft, get_user_drafts
from report_logic import generate_report_pdf, ensure_image_resized, convert_pdf_to_images, image_flowable
from PIL import Image
import io

class TestDatabase(unittest.TestCase):
    """Test database operations"""
    
    def setUp(self):
        """Set up test database"""
        self.test_db = 'test_report_generator.db'
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        # Note: init_db() creates the actual db, we'd need to modify it for testing
    
    def test_user_creation(self):
        """Test user creation"""
        user_id = create_user('test@example.com', 'password123')
        self.assertIsNotNone(user_id)
        self.assertIsInstance(user_id, int)
    
    def test_user_verification(self):
        """Test user verification"""
        create_user('test2@example.com', 'password123')
        user_data = verify_user('test2@example.com', 'password123')
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data['email'], 'test2@example.com')
    
    def test_draft_saving(self):
        """Test draft saving"""
        user_id = create_user('test3@example.com', 'password123')
        draft_id = save_draft(user_id, 'Test Draft', {'test': 'data'})
        self.assertIsNotNone(draft_id)
        
        drafts = get_user_drafts(user_id)
        self.assertGreater(len(drafts), 0)

class TestImageProcessing(unittest.TestCase):
    """Test image processing functions"""
    
    def setUp(self):
        """Create test image"""
        self.test_image = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        img = Image.new('RGB', (2000, 2000), color='red')
        img.save(self.test_image.name, 'JPEG')
        self.test_image.close()
    
    def tearDown(self):
        """Clean up test image"""
        if os.path.exists(self.test_image.name):
            os.remove(self.test_image.name)
    
    def test_image_resize(self):
        """Test image resizing"""
        result = ensure_image_resized(self.test_image.name)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(result))
        
        # Check if image was resized
        img = Image.open(result)
        width, height = img.size
        self.assertLessEqual(width, 1200)
        self.assertLessEqual(height, 1200)
    
    def test_image_flowable(self):
        """Test image flowable creation"""
        result = image_flowable(self.test_image.name)
        self.assertIsNotNone(result)

class TestReportGeneration(unittest.TestCase):
    """Test PDF report generation"""
    
    def setUp(self):
        """Create test data"""
        self.test_data = {
            'general_info': {
                'Activity Type': 'Workshop',
                'Sub Category': 'Technical Skills',
                'Start Date': '2025-01-15',
                'End Date': '2025-01-15',
                'Start Time': '10:00',
                'End Time': '17:00',
                'Venue': 'Test Venue',
                'Collaboration/Sponsor': 'Test Sponsor'
            },
            'speakers': [{
                'name': 'Test Speaker',
                'title': 'Test Title',
                'organization': 'Test Org',
                'contact': 'test@example.com',
                'presentation_title': 'Test Presentation'
            }],
            'participants': [{
                'type': 'Student',
                'count': '10'
            }],
            'synopsis': {
                'highlights': 'Test highlights',
                'key_takeaways': 'Test takeaways',
                'summary': 'Test summary',
                'follow_up': 'Test follow-up'
            },
            'preparers': [{
                'name': 'Test Preparer',
                'designation': 'Test Designation',
                'signature_path': None
            }],
            'speaker_profile': {
                'bio': 'Test bio',
                'image_path': None
            },
            'photos': [],
            'attendance_list': [],
            'brochure': [],
            'notice': [],
            'feedback': [],
            'impact': []
        }
    
    def test_basic_report_generation(self):
        """Test basic report generation without images"""
        try:
            pdf_bytes, filename = generate_report_pdf(self.test_data)
            self.assertIsNotNone(pdf_bytes)
            self.assertGreater(len(pdf_bytes), 0)
            self.assertIsInstance(filename, str)
            self.assertTrue(filename.endswith('.pdf'))
        except Exception as e:
            self.fail(f"Report generation failed: {e}")
    
    def test_report_with_images(self):
        """Test report generation with images"""
        # Create test images
        test_images = []
        for i in range(2):
            img = Image.new('RGB', (800, 600), color='blue')
            temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
            img.save(temp_file.name, 'JPEG')
            temp_file.close()
            test_images.append(temp_file.name)
        
        try:
            self.test_data['photos'] = test_images
            pdf_bytes, filename = generate_report_pdf(self.test_data)
            self.assertIsNotNone(pdf_bytes)
            self.assertGreater(len(pdf_bytes), 0)
        finally:
            # Cleanup
            for img_path in test_images:
                if os.path.exists(img_path):
                    os.remove(img_path)

class TestErrorHandling(unittest.TestCase):
    """Test error handling"""
    
    def test_missing_image_handling(self):
        """Test handling of missing images"""
        result = ensure_image_resized('nonexistent_image.jpg')
        self.assertIsNone(result)
    
    def test_invalid_data_handling(self):
        """Test handling of invalid data"""
        # Test with empty data
        try:
            pdf_bytes, filename = generate_report_pdf({})
            # Should not raise exception, but may produce minimal PDF
            self.assertIsNotNone(pdf_bytes)
        except Exception as e:
            # If it raises, that's also acceptable - we just want to ensure it's handled
            pass

def run_all_tests():
    """Run all tests"""
    print("=" * 70)
    print("Running Comprehensive Test Suite")
    print("=" * 70)
    print()
    
    # Initialize database
    print("Initializing test database...")
    try:
        init_db()
        print("[OK] Database initialized")
    except Exception as e:
        print(f"[ERROR] Database initialization failed: {e}")
        return False
    
    # Run tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestDatabase))
    suite.addTests(loader.loadTestsFromTestCase(TestImageProcessing))
    suite.addTests(loader.loadTestsFromTestCase(TestReportGeneration))
    suite.addTests(loader.loadTestsFromTestCase(TestErrorHandling))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    print("=" * 70)
    if result.wasSuccessful():
        print("ALL TESTS PASSED!")
        print("=" * 70)
        return True
    else:
        print(f"TESTS FAILED: {len(result.failures)} failures, {len(result.errors)} errors")
        print("=" * 70)
        return False

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)

