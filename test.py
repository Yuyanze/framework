import pdfplumber
import pandas as pd
import time

def pdf_table_to_excel(pdf_path, excel_path):
    all_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables() # 自动识别表格结构
            for table in tables:
                all_data.extend(table) # 合并多页或多表数据
    
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_excel(excel_path, index=False, header=False) # 输出 Excel
        print(f"成功保存至 {excel_path}")
    else:
        print("未检测到表格，可能是扫描件或格式特殊。")

# 使用示例
s=time.time()
pdf_table_to_excel("test.pdf", "output.xlsx")
print(time.time()-s)
