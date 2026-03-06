import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def read_docx(file_path):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    
    try:
        with zipfile.ZipFile(file_path, 'r') as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Namespace for docx
            namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            # Extract text from all 'w:t' elements
            texts = []
            for t in tree.findall('.//w:t', namespace):
                if t.text:
                    texts.append(t.text)
            
            return '\n'.join(texts)
    except Exception as e:
        return f"Error reading {file_path}: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python read_docx.py <file_path>")
    else:
        # Handle UTF-8 output on Windows
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        print(read_docx(sys.argv[1]))
