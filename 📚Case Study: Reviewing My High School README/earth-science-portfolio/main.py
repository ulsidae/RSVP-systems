import matplotlib.pyplot as plt

# a좌표
a1 = tuple(map(float, input("a1 = (x, y)에서 x,y: ").split(',')))  #x,y를 입력받으면 ,를 제외한
a2 = tuple(map(float, input("a2 = (x, y)에서 x,y: ").split(','))) #x y를 각각 x의 값과 y의값에 저장
a3 = tuple(map(float, input("a3 = (x, y)에서 x,y: ").split(',')))
a4 = tuple(map(float, input("a4 = (x, y)에서 x,y: ").split(',')))
a5 = tuple(map(float, input("a5 = (x, y)에서 x,y: ").split(',')))
# b좌표
b1 = tuple(map(float, input("b1 = (x, y)에서 x,y: ").split(',')))
b2 = tuple(map(float, input("b2 = (x, y)에서 x,y: ").split(',')))
b3 = tuple(map(float, input("b3 = (x, y)에서 x,y: ").split(',')))
b4 = tuple(map(float, input("b4 = (x, y)에서 x,y: ").split(',')))
b5 = tuple(map(float, input("b5 = (x, y)에서 x,y: ").split(',')))

# 이미지
fig, gr = plt.subplots(figsize=(6, 6)) #정사각형 형태 인식
img = plt.imread("base.png") #이미지 명(360*360 크기)
gr.imshow(img, extent=[-180, 180, -180, 180]) #x축으로 0~360, y축으로 0~360 --> 360*360으로 출력되게함

# 고친 로직
def plot_line(coords, label):
    x, y = zip(*coords)
    gr.plot(x, y, marker='o', label=label)

plot_line([a1, a2, a3, a4, a5], 'Line A') #a점을 lineA로 설정하고 연결
plot_line([b1, b2, b3, b4, b5], 'Line B') #b점을 lineB로 //

# 그래프 값 설정
gr.set_xlim(-180, 180) #x축
gr.set_ylim(-180, 180) #y축
gr.set_xlabel('x')
gr.set_ylabel('y')
gr.set_title('vizualize')
gr.set_aspect('equal')

# 출력
plt.legend()
plt.show()
