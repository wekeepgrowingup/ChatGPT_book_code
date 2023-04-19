from PIL import Image
import os
import zipfile

# 원본 이미지들이 들어있는 폴더 경로
original_folder_path = "original/"
# 워터마크 이미지 경로
watermark_path = "watermark.png"
# 결과 이미지들이 저장될 폴더 경로
result_folder_path = "result/"
# 결과 zip 파일 경로
zip_file_path = "result.zip"

try:
    # 결과 폴더 생성
    if not os.path.exists(result_folder_path):
        os.makedirs(result_folder_path)

    # 워터마크 이미지 로드 및 resize
    watermark = Image.open(watermark_path).convert("RGBA")
    watermark = watermark.resize((50, 50))

    # 폴더 내 이미지들에 워터마크 추가 및 저장
    for file_name in os.listdir(original_folder_path):
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            # 이미지 로드 및 resize
            image_path = os.path.join(original_folder_path, file_name)
            image = Image.open(image_path).convert("RGBA")
            image = image.resize((500, 500))

            # 워터마크 추가
            image.paste(watermark, (450, 450), mask=watermark)

            # 결과 이미지 저장
            result_path = os.path.join(result_folder_path, file_name)
            image.convert("RGB").save(result_path)

    # 결과 폴더를 zip 파일로 압축
    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        for file_name in os.listdir(result_folder_path):
            file_path = os.path.join(result_folder_path, file_name)
            zip_file.write(file_path, arcname=file_name)

    print("모두 완성!")

except Exception as e:
    print(f"오류 발생: {e}")
