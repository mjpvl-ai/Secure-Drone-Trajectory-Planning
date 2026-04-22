import re
import os

def convert_thesis(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    
    # regex for headers/footers
    roll_no_pattern = re.compile(r'^CS21M1005$', re.IGNORECASE)
    dept_date_pattern = re.compile(r'^Computer science and Engineering.*$', re.IGNORECASE)
    page_num_pattern = re.compile(r'^\s*([ivx]+|[0-9]+)\s*$', re.IGNORECASE)
    rep_header_pattern = re.compile(r'^CHAPTER\s+\d+\..*$', re.IGNORECASE) # e.g. CHAPTER 1. LITERATURE REVIEW
    rep_header_pattern2 = re.compile(r'^Trajectory Planning for Autonomous Drone Delivery.*$', re.IGNORECASE)
    
    # regex for headings
    chapter_pattern = re.compile(r'^CHAPTER\s+(\d+)$', re.IGNORECASE)
    section_pattern = re.compile(r'^(\d+\.\d+)\s*(.*)$')
    subsection_pattern = re.compile(r'^(\d+\.\d+\.\d+)\s*(.*)$')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Remove page breaks
        line = line.replace('\f', '')
        
        # Skip empty lines that are just whitespace after stripping
        if not line:
            processed_lines.append("")
            i += 1
            continue
            
        # Skip headers/footers
        if roll_no_pattern.match(line) or dept_date_pattern.match(line) or \
           rep_header_pattern.match(line) or rep_header_pattern2.match(line):
            i += 1
            continue
            
        # Page numbers
        if page_num_pattern.match(line):
            i += 1
            continue

        # Handle Chapters
        chapter_match = chapter_pattern.match(line)
        if chapter_match:
            chap_num = chapter_match.group(1)
            processed_lines.append(f"\n# CHAPTER {chap_num}")
            i += 1
            # Look for title on next few lines
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line or page_num_pattern.match(next_line):
                    i += 1
                    continue
                if chapter_pattern.match(next_line) or section_pattern.match(next_line) or \
                   rep_header_pattern.match(next_line) or rep_header_pattern2.match(next_line):
                    break # hit another heading or rep header
                processed_lines.append(f"# {next_line}\n")
                i += 1
                break
            continue

        # Handle Subsections
        subs_match = subsection_pattern.match(line)
        if subs_match:
            num = subs_match.group(1)
            rest = subs_match.group(2).strip()
            rest = rest.split(' . .')[0].strip() # remove TOC dots
            # Also check if rest is something we want to skip
            if roll_no_pattern.match(rest) or dept_date_pattern.match(rest) or page_num_pattern.match(rest):
                i += 1
                continue
                
            if not rest:
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    if not next_line or page_num_pattern.match(next_line):
                        j += 1
                        continue
                    if chapter_pattern.match(next_line) or section_pattern.match(next_line) or \
                       rep_header_pattern.match(next_line) or rep_header_pattern2.match(next_line):
                        break
                    rest = next_line.split(' . .')[0].strip()
                    i = j
                    break
            processed_lines.append(f"\n### {num} {rest}\n")
            i += 1
            continue

        # Handle Sections
        sec_match = section_pattern.match(line)
        if sec_match:
            num = sec_match.group(1)
            rest = sec_match.group(2).strip()
            rest = rest.split(' . .')[0].strip() # remove TOC dots
            # Also check if rest is something we want to skip
            if roll_no_pattern.match(rest) or dept_date_pattern.match(rest) or page_num_pattern.match(rest):
                i += 1
                continue

            if not rest:
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()
                    if not next_line or page_num_pattern.match(next_line):
                        j += 1
                        continue
                    if chapter_pattern.match(next_line) or section_pattern.match(next_line) or \
                       rep_header_pattern.match(next_line) or rep_header_pattern2.match(next_line):
                        break
                    rest = next_line.split(' . .')[0].strip()
                    i = j
                    break
            processed_lines.append(f"\n## {num} {rest}\n")
            i += 1
            continue

        # Handle Abstract/ToC etc that might be in caps on their own line
        if line in ["ABSTRACT", "TABLE OF CONTENTS", "LIST OF TABLES", "LIST OF FIGURES", "ABBREVIATIONS", "CERTIFICATE", "DECLARATION OF ORIGINALITY"]:
            processed_lines.append(f"\n# {line}\n")
            i += 1
            continue

        # Handle Figure/Table labels
        if line.startswith("Figure ") or line.startswith("Table "):
            processed_lines.append(f"\n**{line}**\n")
            i += 1
            continue

        # Default: just add the line
        processed_lines.append(line)
        i += 1

    # Final cleanup: remove excessive empty lines
    final_text = "\n".join(processed_lines)
    final_text = re.sub(r'\n{3,}', '\n\n', final_text)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_text)
    
    print(f"Successfully converted to {output_file}")

if __name__ == "__main__":
    convert_thesis("thesis_raw.txt", "Thesis.md")
