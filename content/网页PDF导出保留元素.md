
---
title: "网页PDF导出保留元素"
---

## 🤖 Assistant

I'll create an HTML file with PDF export functionality that preserves the webpage elements. This will use html2pdf.js library for converting the content to PDF. Here's the complete solution:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF Export</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
        }
        #contentToPrint {
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        #exportBtn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-bottom: 20px;
        }
        #exportBtn:hover {
            background-color: #45a049;
        }
        iframe {
            width: 100%;
            height: 600px;
            border: 1px solid #ccc;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <button id="exportBtn">Export to PDF</button>
    <div id="contentToPrint">
        <iframe src="https://metaso.cn/search/8623131157501214720/interactive?dataId=8623131157610266624&targetType=1"></iframe>
    </div>

    <script>
        document.getElementById('exportBtn').addEventListener('click', function() {
            // Get the element to print
            const element = document.getElementById('contentToPrint');
            
            // Options for PDF generation
            const opt = {
                margin: 10,
                filename: 'exported_page.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { 
                    scale: 2,
                    useCORS: true,
                    allowTaint: true,
                    logging: true,
                    scrollX: 0,
                    scrollY: 0
                },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            };

            // Generate PDF
            html2pdf().from(element).set(opt).save();
        });
    </script>
</body>
</html>
```

This solution includes:

1. A button to trigger the PDF export
2. An iframe that displays the target webpage (https://metaso.cn/search/8623131157501214720/interactive)
3. PDF generation using html2pdf.js library with configuration options for:
 - Margins
 - File name
 - Image quality
 - Scaling
 - PDF format (A4)
 - CORS handling for iframe content

Note: Due to browser security restrictions, the PDF export of iframe content may be limited if the target website doesn't explicitly allow framing. If you encounter issues, you might need to:
1. Use a server-side solution
2. Get permission from the target website to frame their content
3. Use a screenshot API as an alternative approach

The html2pdf.js library handles most modern browser requirements and provides good quality PDF output while preserving the visual appearance of the content.
