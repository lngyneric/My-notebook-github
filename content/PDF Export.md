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