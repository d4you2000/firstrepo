import streamlit as st

# MBTI 특성 데이터
mbti_traits = {
    'ISTJ': '실용적이고 신뢰성이 높으며, 체계적이고 신중하게 일을 처리합니다.',
    'ISFJ': '친절하고 배려가 깊으며, 헌신적이고 책임감이 강합니다.',
    'INFJ': '이해심이 깊고 직관력이 뛰어나며, 창의적이고 목표 지향적입니다.',
    'INTJ': '독립적이고 전략적이며, 분석적 사고를 통해 문제를 해결합니다.',
    'ISTP': '실용적이고 적응력이 뛰어나며, 문제 해결에 있어 즉각적인 반응을 보입니다.',
    'ISFP': '자유롭고 개방적이며, 아름다움과 감성을 중요시 여깁니다.',
    'INFP': '이상주의적이고 창의적이며, 개인적인 가치와 의미를 중시합니다.',
    'INTP': '논리적이고 분석적이며, 지식 탐구와 문제 해결에 열정을 가지고 있습니다.',
    'ESTP': '활발하고 에너지가 넘치며, 실용적인 해결책을 선호합니다.',
    'ESFP': '사교적이고 재미있는 것을 좋아하며, 주변 사람들과의 관계를 중요시합니다.',
    'ENFP': '열정적이고 창의적이며, 새로운 아이디어와 가능성에 흥미를 느낍니다.',
    'ENTP': '혁신적이고 대담하며, 문제 해결과 아이디어 탐색에 적극적입니다.',
    'ESTJ': '조직적이고 현실적이며, 명확한 목표를 세우고 계획적으로 일을 처리합니다.',
    'ESFJ': '사교적이고 배려가 깊으며, 주변 사람들과의 조화를 중시합니다.',
    'ENFJ': '따뜻하고 공감 능력이 뛰어나며, 타인의 성장과 발전을 지원합니다.',
    'ENTJ': '결단력이 뛰어나고 목표 지향적이며, 효율적이고 체계적인 접근을 선호합니다.',
}

# MBTI 호환도 데이터
compatibility = {
    'ISTJ': ['ESTJ', 'ISFJ'],
    'ISFJ': ['ESFJ', 'ISTJ'],
    'INFJ': ['ENFJ', 'INFP'],
    'INTJ': ['ENTJ', 'INTP'],
    'ISTP': ['ESTP', 'ISFP'],
    'ISFP': ['ESFP', 'ISTP'],
    'INFP': ['ENFP', 'INFJ'],
    'INTP': ['ENTP', 'INTJ'],
    'ESTP': ['ISTP', 'ESFP'],
    'ESFP': ['ISFP', 'ESTP'],
    'ENFP': ['INFP', 'ENFJ'],
    'ENTP': ['INTP', 'ENTJ'],
    'ESTJ': ['ISTJ', 'ESFJ'],
    'ESFJ': ['ISFJ', 'ESTJ'],
    'ENFJ': ['INFJ', 'ENFP'],
    'ENTJ': ['INTJ', 'ENTP'],
}

# 스트림릿 앱 제목
st.title('MBTI 특성 및 호환성 분석')

# MBTI 입력 받기
mbti_type = st.selectbox('당신의 MBTI 유형을 선택하세요:', list(mbti_traits.keys()))

# MBTI 특성 출력
st.subheader('당신의 MBTI 특성:')
st.write(mbti_traits[mbti_type])

# 호환성 추천
compatible_types = compatibility.get(mbti_type, [])
non_compatible_types = [t for t in mbti_traits.keys() if t not in compatible_types and t != mbti_type]

st.subheader('잘 맞는 MBTI 유형:')
st.write(', '.join(compatible_types) if compatible_types else '없음')

st.subheader('잘 맞지 않는 MBTI 유형:')
st.write(', '.join(non_compatible_types) if non_compatible_types else '모든 유형과 잘 맞아요!')
