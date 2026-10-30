from collections import defaultdict


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 1. s1의 빈도 맵 생성
        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1

        # 2. s2의 첫 번째 윈도우(길이 len(s1)) 맵 생성
        s2_map = defaultdict(int)
        for i in range(len(s1)):
            s2_map[s2[i]] += 1

        # 루프 진입 전 첫 윈도우 비교
        if s1_map == s2_map:
            return True

        # 3. 슬라이딩 윈도우 이동
        for r in range(len(s1), len(s2)):
            # 새로 들어오는 문자 추가
            right_key = s2[r]
            s2_map[right_key] += 1

            # 윈도우를 벗어나는 왼쪽 문자 제거 (개수 1 감소)
            left_key = s2[r - len(s1)]
            s2_map[left_key] -= 1

            # 개수가 0이 되면 딕셔너리에서 완전히 제거 (정확한 맵 비교를 위해 필수)
            if s2_map[left_key] == 0:
                del s2_map[left_key]

            # 매번 비교
            if s1_map == s2_map:
                return True

        return False