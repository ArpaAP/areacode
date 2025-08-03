import pandas as pd

input_file = "filtered_output.csv"
output_file = "result.json"

df = pd.read_csv(input_file, encoding='cp949')

# 필터링된 데이터에서 법정동코드	시도명	시군구명	읍면동명 필드만 선택해 JSON 파일로 저장합니다.
selected_df = df[['법정동코드', '시도명', '시군구명', '읍면동명']]
selected_df = selected_df.rename(columns={
    '법정동코드': 'code',
    '시도명': 'province',
    '시군구명': 'city',
    '읍면동명': 'district'
})
selected_df['code'] = selected_df['code'].astype(str)
selected_df.to_json(output_file, orient='records', force_ascii=False)
