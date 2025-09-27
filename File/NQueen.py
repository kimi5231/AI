# 2022184031 임수영
import queue

# 상태를 나타내는 클래스, f(n) 값을 저장한다.
class State:
    def __init__(self, board, depth = 0, parent = None):
        self.board = board # 현재의 보드 상태
        self.depth = depth # 깊이
        self.parent = parent # 부모 노드

    # 자식 노드를 확장하여서 리스트에 저장하여서 반환한다.
    # Queen은 하나의 열에서만 움직인다.
    def expand(self):
        result = []
        for i in range(N):
            new_board = self.board[:]
            new_board[N*i + self.depth] = self.depth + 1
            result.append(State(new_board, self.depth + 1, self))
        return result

    def find_cross(self, queen_pos):
        cross = set()
        # 가로
        for i in range(N):
            if self.board[(queen_pos//N)*N + i] != 0 and ((queen_pos//N)*N + i) != queen_pos:
                cross.add(frozenset({self.board[queen_pos], self.board[(queen_pos//N)*N + i]}))
        # 우상향 대각선
        for i in range(N):
            pos = queen_pos - N*(i+1) + (i+1)
            if (0 <= pos < N*N) and queen_pos%N < pos%N :
                if self.board[pos] != 0:
                    cross.add(frozenset({self.board[queen_pos], self.board[pos]}))
        # 우하향 대각선
        for i in range(N):
            pos = queen_pos + N*(i+1) + (i+1)
            if (0 <= pos < N*N) and queen_pos%N < pos%N:
                if self.board[pos] != 0:
                    cross.add(frozenset({self.board[queen_pos], self.board[pos]}))
        # 좌상향 대각선
        for i in range(N):
            pos = queen_pos - N * (i + 1) - (i + 1)
            if (0 <= pos < N * N) and queen_pos%N > pos%N:
                if self.board[pos] != 0:
                    cross.add(frozenset({self.board[queen_pos], self.board[pos]}))
        # 좌하향 대각선
        for i in range(N):
            pos = queen_pos + N * (i + 1) - (i + 1)
            if (0 <= pos < N * N) and queen_pos%N > pos%N:
                if self.board[pos] != 0:
                    cross.add(frozenset({self.board[queen_pos], self.board[pos]}))
        return cross

    # f(n)을 계산하여 반환한다.
    def f(self):
        return self.h() + self.g()

    # 휴리스틱 함수 값인 h(n)을 계산하여 반환한다.
    # 겹치는 Queen 쌍의 수를 계산한다.
    def h(self):
        score = 0
        cross = set()
        for i in range(self.depth):
            queen_pos = self.board.index(i + 1)
            cross |= self.find_cross(queen_pos)
        score += len(cross)
        return score

    # 시작 노드로부터의 깊이를 반환한다.
    def g(self):
        return self.depth

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return self.board != other.board

    # 상태와 상태를 비교하기 위하여 less than 연산자를 정의한다.
    def __lt__(self, other):
        return self.f() < other.f()

    def __gt__(self, other):
        return self.f() > other.f()

    # 객체를 출력할 때 사용
    def __str__(self):
        result = f"f(n)={self.f()} h(n)={self.h()} g(n)={self.g()}\n"
        for i in range(N):
            result += (str(self.board[N*i:N*(i+1)]) + "\n")
        return result

# 재귀함수로 최적 경로 출력
def print_best_path(node):
    if node.parent is None:
        print(node)
        return
    print_best_path(node.parent)
    print(node)



N = int(input("N 입력: "))

# 빈 보드 생성
# 0 == 빈칸
board = [0 for _ in range(N*N)]

# open 리스트는 우선순위 큐로 생성한다.
open_queue = queue.PriorityQueue()
open_queue.put(State(board))

closed_queue = [ ]

count = 0

while not open_queue.empty():
    # 가장 최선인 노드를 꺼낸다.
    current = open_queue.get()
    count += 1
    print(count)
    print(current)
    if current.h() == 0 and current.g() == N: # 서로 겹치는 Queen이 없고, N개의 Queen이 모두 배치된 상태
         print("탐색 성공")
         print("최적 경로 출력")
         print_best_path(current)
         print("2022184031 임수영")
         break
    if current.depth < N:
        for state in current.expand():
            if state not in closed_queue and state not in open_queue.queue:
                open_queue.put(state)
    closed_queue.append(current)
else:
    print ('탐색 실패')