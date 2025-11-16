"""
Generate a sample PDF report to preview the output
Run this script to see what the generated report looks like
"""
from report_logic import generate_report_pdf
from datetime import datetime

# Sample data for the report
sample_data = {
    'general_info': {
        'Activity Type': 'Workshop',
        'Sub Category': 'Technical Skills',
        'Start Date': '2025-01-15',
        'End Date': '2025-01-15',
        'Start Time': '10:00',
        'End Time': '17:00',
        'Venue': 'Main Auditorium, Christ University',
        'Collaboration/Sponsor': 'Tech Corp Inc.'
    },
    'speakers': [
        {
            'name': 'Dr. John Smith',
            'title': 'Senior Data Scientist',
            'organization': 'Tech Corp Inc.',
            'contact': 'john.smith@techcorp.com',
            'presentation_title': 'Introduction to Machine Learning'
        },
        {
            'name': 'Dr. Jane Doe',
            'title': 'AI Research Lead',
            'organization': 'AI Research Labs',
            'contact': 'jane.doe@airesearch.com',
            'presentation_title': 'Deep Learning Applications'
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
        'highlights': 'The workshop covered fundamental concepts of machine learning and deep learning, with hands-on sessions on Python programming and TensorFlow. Participants engaged in practical exercises and Q&A sessions.',
        'key_takeaways': '1. Understanding of ML fundamentals\n2. Hands-on experience with TensorFlow\n3. Real-world applications of deep learning\n4. Networking opportunities with industry experts',
        'summary': 'This one-day workshop provided comprehensive training on machine learning and deep learning technologies. The sessions included theoretical concepts, practical demonstrations, and hands-on coding exercises. Participants gained valuable insights into current industry practices and emerging trends in AI/ML.',
        'follow_up': '1. Organize advanced workshop on neural networks\n2. Create study group for continued learning\n3. Plan industry visit to Tech Corp Inc.\n4. Schedule follow-up session in next month'
    },
    'preparers': [
        {
            'name': 'Dr. Alpha Vijayan',
            'designation': 'Associate Professor',
            'signature_path': None  # Would be a path to signature image
        }
    ],
    'speaker_profile': {
        'bio': 'Dr. John Smith is a renowned data scientist with over 15 years of experience in machine learning and artificial intelligence. He has published numerous research papers and led several successful AI projects in industry.',
        'image_path': None  # Would be a path to speaker image
    },
    'photos': [],  # Would contain paths to activity photos
    'attendance_list': [],  # Would contain paths to attendance documents
    'brochure': [],  # Would contain paths to brochure documents
    'notice': [],  # Would contain paths to notice documents
    'feedback': [],  # Would contain paths to feedback documents
    'impact': []  # Would contain paths to impact analysis documents
}

if __name__ == '__main__':
    print("Generating sample PDF report...")
    print("=" * 60)
    
    try:
        pdf_bytes, filename = generate_report_pdf(sample_data)
        
        # Save the PDF
        output_path = f"sample_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        with open(output_path, 'wb') as f:
            f.write(pdf_bytes)
        
        print("Sample report generated successfully!")
        print(f"File saved as: {output_path}")
        print(f"File size: {len(pdf_bytes) / 1024:.2f} KB")
        print("\nThe report includes:")
        print("  - University header")
        print("  - General information section")
        print("  - Speaker details (2 speakers)")
        print("  - Participants profile (65 total participants)")
        print("  - Synopsis with highlights, takeaways, summary, and follow-up")
        print("  - Report preparer information")
        print("  - Speaker profile section")
        print("  - Activity photos section (empty in sample)")
        print("  - New sections: Attendance, Brochure, Notice, Feedback, Impact")
        print("\nOpen the PDF file to view the complete report!")
        
    except Exception as e:
        print(f"Error generating report: {e}")
        import traceback
        traceback.print_exc()

