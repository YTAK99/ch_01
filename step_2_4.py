import json
from pathlib import Path
from step_2_1 import OUT_DIR                                                # 이전에 작성한 모듈을 불러옴
from step_2_2 import get_total_filesize
from step_2_3 import load_dirnames

OUT_2_4 = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_filesize_from_dirnames():                                          # 이전 단계에서 생성된 JSON 형식의 폴더 목록 파일을 불러와 폴더별로 파일 크기를 측정하고, 그 결과를 JSON 형식으로 OUT_2_4 경로에 저장하는 함수를 정의
    dirs = load_dirnames()                                                  # 함수 load_dirnames() 를 사용하여 폴더 목록을 불러와서 변수 dirs에 저장
    result = {}                                                             # 딕셔너리 result를 생성. result에는 폴더 경로와 크기를 각각 키와 값 쌍으로 저장
    for path_str in dirs:                                                   # dirs에 있는 폴더에 대해 반복 작업 수행
        path = Path(path_str)                                               # path_str에 저장된 폴더 경로 문자열을 Path 객체로 변환하고, 변수 path에 저장
        filesize = get_total_filesize(path, pattern="**/*")                 # 변수 filesize에 폴더의 크기를 저장. 이때 매개변수 pattern에 글로브 패턴 "**/*"을 전달해서 하위 폴더를 포함하여 모든 파일을 검색하도록 지정
        result[path.as_posix()] = filesize                                  # 딕셔너리에 폴더의 경로와 크기를 저장
    with open(OUT_2_4, "w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)

def load_filesize_per_dir() -> dict[str, int]:                              # OUT_2_4 경로에 저장된 폴더별 파일 크기 파일을 불러와서 딕셔너리로 반환하는 함수를 정의
    if OUT_2_4.is_file():
        with open(OUT_2_4, encoding="utf-8") as fp:
            return json.load(fp)
    return {}

if __name__ == "__main__":
    dump_filesize_from_dirnames()                                           # 함수를 호출하여 홈 디렉터리 하위 폴더의 크기를 측정