# Cyberverse Metadata Inspector

**Cyberverse Metadata Inspector** is a powerful, beginner-friendly web app that lets you instantly analyze and reveal hidden metadata from any file. Built with Streamlit and ExifTool, it’s perfect for digital forensics, privacy checks, and gaining deep insights into your files—all from your browser.

## What is EXIF Metadata?

**EXIF** (Exchangeable Image File Format) metadata is a set of hidden information automatically embedded in image files by digital cameras and smartphones. This metadata can include:

- The date and time the photo was taken
- Camera make and model
- Camera settings (aperture, shutter speed, ISO, etc.)
- GPS coordinates (location where the photo was captured)
- Software used for editing or processing

While EXIF data is useful for photographers to review and organize their images, it can also pose significant privacy and security risks. For example, sharing a photo online with embedded GPS data can unintentionally reveal your home or workplace location to anyone who downloads the image[1][3][4][5].

---

## Why is EXIF Metadata Important in CTFs (Capture The Flag)?

In cybersecurity competitions like **CTFs**, EXIF metadata often plays a crucial role in forensic and OSINT (Open Source Intelligence) challenges:

- **Hidden Clues:** CTF organizers may embed secret flags, hints, or critical information in the EXIF metadata of challenge images.
- **Timeline Reconstruction:** Forensic tasks may require competitors to determine when and where a photo was taken, or which device was used, based on EXIF tags.
- **Real-World Relevance:** Understanding and analyzing EXIF data mirrors real-world digital forensics, where investigators use metadata to trace incidents, verify authenticity, or uncover tampering[1][5][6].

**Example CTF Scenarios:**
- Download an image and extract the flag hidden in a custom EXIF tag.
- Analyze the GPS coordinates in EXIF data to find a physical location.
- Use timestamps and device info to reconstruct an event timeline.

---

## Privacy & Security Implications

EXIF metadata can inadvertently expose sensitive personal or organizational information, such as:
- Exact locations (via GPS)
- Device ownership and usage patterns
- Dates and times of activities

Malicious actors can exploit this data for stalking, identity theft, or intelligence gathering. Even if you’re not a CTF competitor, learning to inspect and sanitize EXIF metadata is a vital digital hygiene skill[1][3][4][5].

---

## How Cyberverse Metadata Inspector Helps

> **Knowledge of EXIF metadata is a must-have for anyone interested in cybersecurity, digital forensics, or privacy. Mastering metadata analysis can give you the edge in CTFs and help protect your digital footprint in everyday life.**

- **Simple Drag-and-Drop:** Upload any file type for instant analysis.
- **Deep Metadata Extraction:** Uncover EXIF data, timestamps, device info, and more.
- **Modern Cyberpunk UI:** Enjoy a sleek, futuristic interface.
- **Privacy First:** No files are stored—everything is processed in-memory.
- **Open Source:** Easily deploy, modify, or integrate into your own projects.

## Live Demo

- [ ] [Try the App Here!](https://metadata-inspector-tool.onrender.com/)  

## Example Use Cases

- **Digital Forensics:** Inspect files for hidden data or tampering.
- **Privacy Audits:** Check what info your files may be leaking.
- **Educational:** Learn about metadata and file structures.

---
