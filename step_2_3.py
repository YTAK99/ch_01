import json
from pathlib import Path
from step_2_1 import OUT_DIR

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.json"       # 출력 파일 경로를 만들고 변수 OUT_2_3에 저장

def dump_dirnames(base_dir: Path) -> None:              # 폴더 목록을 저장하는 함수 dump_dirnames()를 정의한다. 매개변수 base_dir는 폴더 경로를 저장
    dirs = []                                           # 하위 폴더 목록을 저장할 리스트 dirs를 초기화
    for path in base_dir.iterdir():                     # base_dir 경로에 있는 모든 파일을 반복 처리. 함수 iterdir()는 주어진 폴더의 모든 파일과 하위 폴더 목록을 반환.
        if path.is_dir():                               # path 변수에 저장된 경로가 유효하면 코드 11행을 실행
            dirs.append(path.as_posix())                # dirs 리스트에 폴더 경로를 추가. 이 코드는 폴더 경로를 텍스트 파일로 저장하므로, 함수 as_posix()를 사용하여 path 객체를 문자열로 반환
    dirs_sorted = sorted(dirs)                          # 함수 sorted()를 사용하여 dirs 리스트를 오름차순 정렬
    with open(OUT_2_3, "w", encoding="utf-8") as fp:                        # OUT_2_3 경로에 쓰기 모드로 파일을 열고, 이를 변수 fp에 저장
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)            # json 패키지의 함수 dump()를 사용하여 dirs_sorted에 저장된 폴더 목록을 JSON형식의 문자열로 저장

def load_dirnames() -> list[str]:                                   # 폴더 목록이 저장된 JSON파일을 불러오는 함수 load_dirnames()를 정의
    if OUT_2_3.is_file():                                           # OUT_2_3 경로에 파일이 있는지 확인
        with open(OUT_2_3, encoding="utf-8") as fp:                 # OUT_2_3 경로에 있는 파일을 불러옴
            return json.load(fp)                                    # json 패키지의 함수 laod()를 사용하여, JSON 형식으로 저장된 파일을 불러와서 파이썬 데이터 타입으로 변환한 후, 그 결과를 반환
    return []                                                       # 파일이 없으면 빈 리스트를 반환

if __name__ == "__main__":
    dump_dirnames(Path.home())                                      # 함수 dump_dirnames()를 실행. 이때 함수 home()을 사용해 홈 디렉터리의 경로를 입력값으로 전달



#dir /ah 숨겨진 폴더 확인