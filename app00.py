import streamlit as st
import random
import time

st.title("🎰 리얼 777 슬롯머신")
st.write("버튼을 누르면 숫자가 실제로 돌아갑니다!")

# 1. 숫자가 표시될 빈 공간(컨테이너)을 먼저 만들어둡니다.
placeholder = st.empty()

# initial state 설정
if "reels" not in st.session_state:
    st.session_state.reels = [7, 7, 7]

# 2. 처음 화면이나 멈췄을 때의 상태를 그려주는 함수
def display_reels(numbers):
    with placeholder.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<h1 style='text-align: center; font-size: 80px;'> {numbers[0]} </h1>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<h1 style='text-align: center; font-size: 80px;'> {numbers[1]} </h1>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<h1 style='text-align: center; font-size: 80px;'> {numbers[2]} </h1>", unsafe_allow_html=True)

# 첫 실행 시 기본 7 7 7 화면 표시
display_reels(st.session_state.reels)

# 3. 돌리기 버튼
if st.button("🎰 슬롯 돌리기!!", use_container_width=True):
    # 15번 동안 무작위 숫자를 빠르게 보여주며 돌아가는 효과 연출
    for i in range(15):
        random_reels = [random.randint(1, 9) for _ in range(3)]
        display_reels(random_reels)
        # 처음엔 빠르게 돌다가 갈수록 살짝 느려지게 세팅 (현실감 추가)
        time.sleep(0.05 + (i * 0.01)) 
    
    # 최종 결과 결정 및 저장
    st.session_state.reels = [random.randint(1, 9) for _ in range(3)]
    display_reels(st.session_state.reels)

    # 4. 결과 판정
    if st.session_state.reels == [7, 7, 7]:
        st.balloons()
        st.success("🎉 대박! 777 잭팟이 터졌습니다! 🎉")
    elif len(set(st.session_state.reels)) == 1:
        st.success(f"🎉 오! {st.session_state.reels[0]} 트리플! 미니 잭팟! 🎉")
