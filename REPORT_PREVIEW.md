# Report Generator - Sample Output Preview

## Report Structure

The generated PDF report includes the following sections in order:

### 1. **Header Section**
- Christ (Deemed to be University), Bangalore
- School of Engineering and Technology
- Department of AI, ML & Data Science
- "Activity Report" title

### 2. **General Information**
Formatted as a table with:
- Activity Type
- Sub Category
- Date/s (formatted as "DD Month YYYY" or date range)
- Time (formatted as "HH:MM – HH:MM")
- Venue
- Collaboration/Sponsor (if provided)

### 3. **Speaker/Guest/Presenter Details**
For each speaker, a table showing:
- Name
- Title/Position
- Organization
- Contact Info
- Title of Presentation

### 4. **Participants Profile**
For each participant type, a table showing:
- Type of Participants (Faculty/Student/Research Scholar)
- No. of Participants

### 5. **Synopsis of the Activity (Description)**
A table with:
- Highlights of the Activity
- Key Takeaways
- Summary of the Activity
- Follow-up plan

### 6. **Report Prepared By**
For each preparer:
- Name of the Organiser
- Designation/Title
- Digital Signature (image, if uploaded)

### 7. **Speaker Profile**
- Speaker biography text (if provided)
- Speaker photo (if uploaded)

### 8. **Photos of the Activity** (New Page)
- Section heading with activity title and date
- All uploaded activity photos (resized and optimized)
- Each photo on a separate section with spacing

### 9. **New Sections** (Each on New Page)
- **Attendance List** - All uploaded attendance documents (PDF pages converted to images)
- **Brochure** - All uploaded brochure documents
- **Notice for Approval** - All uploaded notice documents
- **Feedback Analysis** - All uploaded feedback documents
- **Impact Analysis** - All uploaded impact analysis documents

## Report Formatting

- **Page Size**: A4
- **Margins**: 0.9 inches on all sides
- **Font**: Times-Roman (body), Times-Bold (headings)
- **Colors**: Professional black text with blue accents
- **Tables**: Bordered tables with proper spacing
- **Images**: Centered, automatically resized to fit page width
- **Page Numbers**: Bottom-right corner on all pages

## Visual Features

- Clean, professional layout
- Consistent spacing and formatting
- Proper page breaks between major sections
- Images are optimized and compressed
- PDF pages from uploaded documents are converted to images (one page = one image)

## To Generate a Sample Report

Run the sample report generator:

```bash
python generate_sample_report.py
```

This will create a PDF file named `sample_report_YYYYMMDD_HHMMSS.pdf` that you can open to see the exact format and structure.

## Example Report Sections

### General Information Table
```
┌─────────────────────────────┬─────────────────────────────────────┐
│ Activity Type               │ Workshop                            │
│ Sub Category                │ Technical Skills                    │
│ Date/s                      │ 15 January 2025                     │
│ Time                        │ 10:00 – 17:00                       │
│ Venue                       │ Main Auditorium, Christ University  │
│ Collaboration/Sponsor       │ Tech Corp Inc.                      │
└─────────────────────────────┴─────────────────────────────────────┘
```

### Speaker Details Table
```
┌─────────────────────────────┬─────────────────────────────────────┐
│ Name                        │ Dr. John Smith                      │
│ Title/Position              │ Senior Data Scientist               │
│ Organization                │ Tech Corp Inc.                      │
│ Contact Info                │ john.smith@techcorp.com             │
│ Title of Presentation       │ Introduction to Machine Learning    │
└─────────────────────────────┴─────────────────────────────────────┘
```

## Notes

- All sections are optional except required fields (marked with * in the form)
- Images are automatically resized if too large
- PDF documents are converted to images (one page per image)
- The report maintains professional academic formatting standards
- Page numbers are automatically added to all pages

