# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 심요섭
# 프로젝트 주제: 신소재 초전도 조건(온도 및 각도) 판별기

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


experiments = []

def add_data(exp_list):
    print("--- 📝 마법각 그래핀 실험 데이터 입력 ---")
    print("각도(도)와 온도(K)를 띄어쓰기로 입력하세요. (예: 1.1 1.5)")
    
    
    for i in range(1, 4):
        
        angle, temp = map(float, input(f"[실험 {i}번] 각도와 온도 입력: ").split())
        
        
        exp_list.append([i, angle, temp, "결과 대기"])
        
    print("✅ 데이터 입력 완료!\n")


def check_superconductivity(exp_list):
    print("--- 🔬 그래핀 초전도 실험 결과 ---")
    
    
    for row in exp_list:
        angle = row[1]  
        temp = row[2]   
        
        
        if angle == 1.1 and temp <= 1.7:
            row[3] = "🔥 초전도 상태 달성!"
        else:
            row[3] = "일반 상태"
            
        
        print(f"실험 {row[0]}번 | 각도: {angle}도, 온도: {temp}K ➡️ 결과: {row[3]}")




add_data(experiments)


check_superconductivity(experiments)

