"""
Generate a comprehensive test PDF report with all images
This will create a complete report to verify the format matches requirements
"""
from report_logic import generate_report_pdf
from datetime import datetime
import os
from PIL import Image, ImageDraw, ImageFont
import tempfile

def create_test_image(width=800, height=600, text="Test Image", color=(70, 130, 180)):
    """Create a test image with text"""
    img = Image.new('RGB', (width, height), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
        except:
            font = ImageFont.load_default()
    
    # Calculate text position (center)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    draw.text(position, text, fill=(255, 255, 255), font=font)
    return img

def create_test_images():
    """Create test images for the report"""
    temp_dir = tempfile.mkdtemp()
    image_paths = []
    
    # Create activity photos
    photo_labels = [
        "Activity Photo 1 - Workshop Session",
        "Activity Photo 2 - Group Discussion",
        "Activity Photo 3 - Hands-on Practice",
        "Activity Photo 4 - Q&A Session"
    ]
    for i, label in enumerate(photo_labels):
        img = create_test_image(1200, 800, label, color=(52, 152, 219))
        path = os.path.join(temp_dir, f'photo_{i+1}.jpg')
        img.save(path, 'JPEG', quality=85)
        image_paths.append(path)
    
    # Create speaker image
    speaker_img = create_test_image(600, 600, "Speaker Photo", color=(46, 204, 113))
    speaker_path = os.path.join(temp_dir, 'speaker.jpg')
    speaker_img.save(speaker_path, 'JPEG', quality=85)
    
    # Create signature
    sig_img = create_test_image(400, 150, "Digital Signature", color=(241, 196, 15))
    sig_path = os.path.join(temp_dir, 'signature.jpg')
    sig_img.save(sig_path, 'JPEG', quality=85)
    
    # Create attendance list image
    att_img = create_test_image(1000, 1400, "Attendance List\n\nParticipant Names\n\n1. John Doe\n2. Jane Smith\n3. Bob Johnson", color=(155, 89, 182))
    att_path = os.path.join(temp_dir, 'attendance.jpg')
    att_img.save(att_path, 'JPEG', quality=85)
    
    # Create brochure image
    brochure_img = create_test_image(1000, 1400, "Event Brochure\n\nWorkshop Details\n\nDate: 15 Jan 2025\nTime: 10:00 AM - 5:00 PM\nVenue: Main Auditorium", color=(231, 76, 60))
    brochure_path = os.path.join(temp_dir, 'brochure.jpg')
    brochure_img.save(brochure_path, 'JPEG', quality=85)
    
    # Create notice image
    notice_img = create_test_image(1000, 1400, "Notice for Approval\n\nThis is to inform that\na workshop will be conducted\non the specified date.", color=(230, 126, 34))
    notice_path = os.path.join(temp_dir, 'notice.jpg')
    notice_img.save(notice_path, 'JPEG', quality=85)
    
    # Create feedback image
    feedback_img = create_test_image(1000, 1400, "Feedback Analysis\n\nOverall Rating: 4.5/5\n\nPositive Comments:\n- Very informative\n- Well organized\n- Great speakers", color=(26, 188, 156))
    feedback_path = os.path.join(temp_dir, 'feedback.jpg')
    feedback_img.save(feedback_path, 'JPEG', quality=85)
    
    # Create impact analysis image
    impact_img = create_test_image(1000, 1400, "Impact Analysis\n\nWorkshop Impact:\n\n- 65 participants trained\n- 95% satisfaction rate\n- Increased knowledge by 40%\n- Follow-up sessions planned", color=(52, 73, 94))
    impact_path = os.path.join(temp_dir, 'impact.jpg')
    impact_img.save(impact_path, 'JPEG', quality=85)
    
    return {
        'photos': image_paths,
        'speaker': speaker_path,
        'signature': sig_path,
        'attendance': att_path,
        'brochure': brochure_path,
        'notice': notice_path,
        'feedback': feedback_path,
        'impact': impact_path,
        'temp_dir': temp_dir
    }

if __name__ == '__main__':
    print("=" * 70)
    print("Generating Comprehensive Test Report with All Images")
    print("=" * 70)
    print()
    
    try:
        # Create test images
        print("Creating test images...")
        test_images = create_test_images()
        print(f"[OK] Created {len(test_images['photos'])} activity photos")
        print(f"[OK] Created speaker image")
        print(f"[OK] Created signature image")
        print(f"[OK] Created all section images (attendance, brochure, notice, feedback, impact)")
        print()
        
        # Prepare sample data with images
        print("Preparing report data...")
        sample_data = {
            'general_info': {
                'Activity Type': 'Workshop',
                'Sub Category': 'Technical Skills Development',
                'Start Date': '2025-01-15',
                'End Date': '2025-01-15',
                'Start Time': '10:00',
                'End Time': '17:00',
                'Venue': 'Main Auditorium, Christ (Deemed to be University), Bangalore',
                'Collaboration/Sponsor': 'Tech Corp Inc. & AI Research Labs'
            },
            'speakers': [
                {
                    'name': 'Dr. John Smith',
                    'title': 'Senior Data Scientist',
                    'organization': 'Tech Corp Inc.',
                    'contact': 'john.smith@techcorp.com',
                    'presentation_title': 'Introduction to Machine Learning and Deep Learning'
                },
                {
                    'name': 'Dr. Jane Doe',
                    'title': 'AI Research Lead',
                    'organization': 'AI Research Labs',
                    'contact': 'jane.doe@airesearch.com',
                    'presentation_title': 'Advanced Deep Learning Applications in Industry'
                }
            ],
            'participants': [
                {
                    'type': 'Student',
                    'count': '45'
                },
                {
                    'type': 'Faculty',
                    'count': '8'
                },
                {
                    'type': 'Research Scholar',
                    'count': '12'
                }
            ],
            'synopsis': {
                'highlights': 'The workshop covered fundamental and advanced concepts of machine learning and deep learning, with comprehensive hands-on sessions on Python programming, TensorFlow, and PyTorch. Participants engaged in practical exercises, real-world case studies, and interactive Q&A sessions with industry experts.',
                'highlights_format': 'plain',
                'key_takeaways': 'Understanding of ML fundamentals\nHands-on experience with TensorFlow and PyTorch\nReal-world applications of deep learning\nNetworking opportunities with industry experts\nBest practices for implementing ML solutions',
                'key_takeaways_format': 'bullet',
                'summary': 'This comprehensive one-day workshop provided extensive training on machine learning and deep learning technologies. The sessions included theoretical concepts, practical demonstrations, hands-on coding exercises, and real-world case studies. Participants gained valuable insights into current industry practices, emerging trends in AI/ML, and practical skills for implementing ML solutions in their projects.',
                'summary_format': 'plain',
                'follow_up': 'Organize advanced workshop on neural networks\nCreate study group for continued learning\nPlan industry visit to Tech Corp Inc.\nSchedule follow-up session in next month\nShare additional resources via email',
                'follow_up_format': 'numbered'
            },
            'preparers': [
                {
                    'name': 'Dr. Alpha Vijayan',
                    'designation': 'Associate Professor, Department of AI, ML & Data Science',
                    'signature_path': test_images['signature']
                },
                {
                    'name': 'Dr. Saksham Sharma',
                    'designation': 'Assistant Professor, Department of AI, ML & Data Science',
                    'signature_path': test_images['signature']
                }
            ],
            'speaker_profile': {
                'bio': 'Dr. John Smith is a renowned data scientist with over 15 years of experience in machine learning and artificial intelligence. He has published numerous research papers in top-tier conferences and journals, and led several successful AI projects in industry. His expertise includes deep learning, computer vision, natural language processing, and reinforcement learning. He has worked with leading tech companies and has been a keynote speaker at various international conferences.',
                'image_path': test_images['speaker']
            },
            'photos': test_images['photos'],
            'attendance_list': [test_images['attendance']],
            'brochure': [test_images['brochure']],
            'notice': [test_images['notice']],
            'feedback': [test_images['feedback']],
            'impact': [test_images['impact']]
        }
        
        print("[OK] Data prepared")
        print()
        
        # Generate PDF
        print("Generating PDF report...")
        result = generate_report_pdf(sample_data)
        if isinstance(result, tuple):
            pdf_bytes, filename = result
        else:
            pdf_bytes = result
            filename = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        print("[OK] PDF generated successfully")
        print()
        
        # Save the PDF
        output_path = f"test_report_with_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        with open(output_path, 'wb') as f:
            f.write(pdf_bytes)
        
        print("=" * 70)
        print("REPORT GENERATED SUCCESSFULLY!")
        print("=" * 70)
        print(f"\nFile saved as: {output_path}")
        print(f"File size: {len(pdf_bytes) / 1024:.2f} KB")
        print(f"\nThe report includes:")
        print("  [OK] University header with proper formatting")
        print("  [OK] General information section (formatted table)")
        print("  [OK] Speaker details (2 speakers with complete information)")
        print("  [OK] Participants profile (3 types, 65 total participants)")
        print("  [OK] Synopsis section (highlights, takeaways, summary, follow-up)")
        print("  [OK] Report preparers (2 preparers with digital signatures)")
        print("  [OK] Speaker profile (biography with speaker photo)")
        print("  [OK] Activity photos (4 photos on separate pages)")
        print("  [OK] Attendance List (1 image)")
        print("  [OK] Brochure (1 image)")
        print("  [OK] Notice for Approval (1 image)")
        print("  [OK] Feedback Analysis (1 image)")
        print("  [OK] Impact Analysis (1 image)")
        print("\n" + "=" * 70)
        print("Open the PDF file to review the complete report format!")
        print("=" * 70)
        
        # Cleanup temp images (optional - keep for debugging)
        # import shutil
        # shutil.rmtree(test_images['temp_dir'])
        # print(f"\nCleaned up temporary images from {test_images['temp_dir']}")
        
    except Exception as e:
        print(f"\n[ERROR] Error generating report: {e}")
        import traceback
        traceback.print_exc()

