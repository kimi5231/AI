# 2022184031 임수영

import sys

# 상태를 나타내는 클래스
class State:
    def __init__(self, board, goal, depth=0):
        self.board = board
        self.depth = depth
        self.goal = goal

    # i1과 i2를 교환하여서 새로운 상태를 반환한다.
    def get_new_board(self, i1, i2, depth):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, depth)

    # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다.
    def expand(self, depth):
        result = []
        if depth > 5: return result  # 깊이가 5 이상이면 더 이상 확장을 하지 않는다.
        i = self.board.index(0)  # 숫자 0(빈칸)의 위치를 찾는다.
        if not i in [6, 7, 8]:  # DOWN 연산자
            result.append(self.get_new_board(i, i + 3, depth))
        if not i in [2, 5, 8]:  # RIGHT 연산자
            result.append(self.get_new_board(i, i + 1, depth))
        if not i in [0, 1, 2]:  # UP 연산자
            result.append(self.get_new_board(i, i - 3, depth))
        if not i in [0, 3, 6]:  # LEFT 연산자
            result.append(self.get_new_board(i, i - 1, depth))
        return result

    # 객체를 출력할 때 사용한다.
    def __str__(self):
        return str(self.board[:3]) + "\n" + \
        str(self.board[3:6]) + "\n" + \
        str(self.board[6:]) + "\n" + \
        "------------------"

    def __eq__(self, other):  # 이것을 정의해야 in 연산자가 올바르게 계산한다.
        return self.board == other.board
    def __ne__(self, other):  # 이것을 정의해야 in 연산자가 올바르게 계산한다.
        return self.board != other.board

# 재귀함수로 최적 경로 출력
def print_best_path(node):
    if(node.depth == 0):
        print(node)
        return
    while True:
        parent = closed_queue.pop(-1)
        if(parent.depth == node.depth - 1):
            print_best_path(parent)
            break
    print(node)

# 초기 상태
puzzle = [2, 8, 3,
          1, 6, 4,
          7, 0, 5]

# 목표 상태
goal = [1, 2, 3,
        8, 0, 4,
        7, 6, 5]

open_queue = [ ]
open_queue.append(State(puzzle, goal))

closed_queue = [ ]
depth = 0

count = 1

while True:
    # 제한적인 깊이 탐색
    while len(open_queue) != 0:
        current = open_queue.pop(0) # OPEN 리스트의 앞에서 삭제
        print(count)
        print(depth) # 최대 깊이 출력
        count += 1
        print(current)
        if current.board == goal:
            print("탐색 성공")
            print("최적 경로 출력")
            print_best_path(current)
            print("2022184031 임수영")
            sys.exit()
        closed_queue.append(current) # CLOSED 리스트의 맨 뒤에 추가
    # 확장
    while len(closed_queue) != 0:
        node = closed_queue.pop(0)
        open_queue.append(node)
        if node.depth == depth:
            for state in node.expand(depth + 1):
                if (state in closed_queue) or (state in open_queue):  # 이미 거쳐간 노드이면
                    continue  # 노드를 버린다.
                else:
                    open_queue.append(state)

    depth += 1