import json
from pathlib import Path
from step_2_1 import OUT_DIR                                                # 이전에 작성한 모듈을 불러옴
from step_2_4 import load_filesize_per_dir

OUT_3_1 = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_plot_data():                                                       # 데이터를 전처리하는 함수 dump_plot_data()를 정의
    size_per_path = load_filesize_per_dir()
    size_per_stem = {Path(path).stem: size for path,                        # 10~12 : 딕셔너리에 키로 지정된 경로를 폴더 이름으로 변경하고, 변수 size_per_stem에 저장
                     size in size_per_path.items()                          #          이때 폴더 크기가 0보다 큰 데이터만 추출
                     if size > 0}
    plot_data = dict(                           # 13~16 : 두 개의 키 stem과 size를 갖는 새로운 딕셔너리 plot_data를 생성
        stem = list(size_per_stem.keys()),
        size = list(size_per_stem.values())
    )
    with open(OUT_3_1, "w", encoding="utf-8") as fp:                        # 17~18 : 딕셔너리 plot_data에 저장된 데이터를 JSON 형식으로 OUT_3_1 경로에 저장
        json.dump(plot_data, fp, ensure_ascii=False, indent=2)

def load_plot_data() -> dict:                                               # 20~24 : OUT_3_1 경로에 저장된 데이터를 불러와서 반환하는 함수 load_plot_data()를 정의
    if OUT_3_1.is_file():
        with open(OUT_3_1, encoding="utf-8") as fp:
            return json.load(fp)
    return {}

if __name__ == "__main__":
    dump_plot_data()