from pathlib import Path
from step_2_1 import WORK_DIR       # 이전 단계에서 작성한 모듈 불러오기

def get_total_filesize(base_dir: Path, pattern: str = "*") -> int:          # 매개변수 base_dir은 Path 객체를, pattern은 글로브 패턴 문자열을 저장
    total_bytes = 0                         # total_bytes 초기화. 여기에 파일 크기 저장할 것임
    for fullpath in base_dir.glob(pattern):         # glob()는 입력값으로 전달된 글로브 패턴과 일치하는 파일명을 리스트로 반환
        if fullpath.is_file():          # is_file() 함수를 사용하여 파일이 유효한지 검사
            total_bytes += fullpath.stat().st_size      # 파일의 크기를 바이트 단위로 더함
    return total_bytes                      # total_bytes 반환

if __name__ =="__main__":               # 소스 코드 최초 실행 시 12~14행 코드를 수행
    base_dir = WORK_DIR                 # 변수 base_dir에 현재 작업중인 폴더 경로를 저장
    filesize = get_total_filesize(base_dir, pattern="*")        # 함수 호출하고 그 결과값을 fielsize에 저장
    print(f"{base_dir.as_posix()=}, {filesize=} bytes")         # 폴더 크기를 화면에 출력. 함수 as_posix()는 base_dir에 저장된 Path 객체를 문자열로 반환