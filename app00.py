import streamlit as st
import random
import time

# 1. 앱 제목 설정
st.title("🎰 행운의 777 슬롯머신")
st.write("버튼을 눌러 777을 맞춰보세요!")

# 2. 게임 상태 초기화 (처음 실행할 때 기본값 설정)
if "reels" not in st.session_state:
    st.session_state.reels = [7, 7, 7]

# 3. 슬롯 레이아웃 생성 (3개의 열)
col1, col2, col3 = st.columns(3)

with col1:
    st.header(f" {st.session_state.reels[0]} ")
with col2:
    st.header(f" {st.session_state.reels[1]} ")
with col3:
    st.header(f" {st.session_state.reels[2]} ")

# 4. 돌리기 버튼
if st.button("🎰 돌리기!", use_container_width=True):
    # 긴장감을 위한 짧은 로딩 효과
    with st.spinner("돌아가는 중..."):
        time.sleep(0.7)
        
    # 1부터 9까지의 숫자 중 무작위로 3개 선택
    st.session_state.reels = [random.randint(1, 9) for _ in range(3)]
    
    # 숫자가 바뀐 상태로 화면 새로고침
    st.rerun()

# 5. 결과 판정
if st.session_state.reels == [7, 7, 7]:
    st.balloons()  # 화면에 풍선 애니메이션 효과
    st.success("🎉 대박! 777 잭팟이 터졌습니다! 🎉")
elif len(set(st.session_state.reels)) == 1:
    st.success("🎉 오! 숫자가 모두 일치합니다! (미니 잭팟) 🎉")
