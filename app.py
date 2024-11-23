import pandas as pd

# CSV 파일을 읽어옵니다.
input_file = "국토교통부_전국 법정동_20240802.csv"  # 원본 파일 이름
output_file = "filtered_output.csv"  # 필터링 후 저장할 파일 이름

df = pd.read_csv(input_file, encoding='cp949')

# 읍면동명이 존재하고 리명이 존재하지 않으며, 삭제일자가 존재하지 않는 행을 필터링합니다.
filtered_df = df[(df['읍면동명'].notna()) & (df['리명'].isna()) & (df['삭제일자'].isna())]

# 필터링된 데이터를 새로운 CSV 파일로 저장합니다.
filtered_df.to_csv(output_file, index=False, encoding='cp949')

print(f"필터링된 데이터가 {output_file}에 저장되었습니다.")
