import numpy as np
import matplotlib.pyplot as plt

# 리스트 5-1-(9)
# 구배법 ----
np.random.seed(seed=1)  # 난수를 고정
X_min = 4  # X의 하한(표시 용)
X_max = 30  # X의 상한(표시 용)
X_n = 16  # X의 상한(표시 용)
X = 5 + 25 * np.random.rand(X_n)
Prm_c = [170, 108, 0.2]  # 생성 매개 변수
T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) + 4 * np.random.randn(X_n)
np.savez('ch5_data.npz', X=X, X_min=X_min, X_max=X_max, X_n=X_n, T=T)  # (B)
X = np.round(X, 2)
T = np.round(T, 2)

def dmse_line(x, t, w):
    y = w[0] * x + w[1]
    d_w0 = 2 * np.mean((y - t) * x)
    d_w1 = 2 * np.mean(y - t)
    if np.isnan(d_w0):
        print("d_w0 is NaN")
    elif np.isnan(d_w1):
        print("d_w1 is NaN")
    return d_w0, d_w1

def mse_line(x, t, w):
    y = w[0] * x + w[1]
    mse = np.mean((y - t) ** 2)
    if np.isnan(mse):
        print("NaN detected in mse_line")
    return mse

def fit_line_num(x, t):
    w_init = [10.0, 165.0]  # 초기 매개 변수
    alpha = 0.00405  # 학습률
    i_max = 100000  # 반복의 최대 수
    eps = 0.1  # 반복을 종료 기울기의 절대 값의 한계
    w_i = np.zeros([i_max, 2])
    w_i[0, :] = w_init
    for i in range(1, i_max):
        dmse = dmse_line(x, t, w_i[i - 1])
        if np.any(np.isnan(dmse)):
            print("NaN detected in dmse during iteration", i)
            break
        w_i[i, 0] = w_i[i - 1, 0] - alpha * dmse[0]
        w_i[i, 1] = w_i[i - 1, 1] - alpha * dmse[1]
        if max(np.absolute(dmse)) < eps:
            break
    w0 = w_i[i, 0]
    w1 = w_i[i, 1]
    w_i = w_i[:i, :]
    return w0, w1, dmse, w_i

# 메인 ----
plt.figure(figsize=(4, 4))  # MSE의 등고선 표시

xn = 100  # 등고선 해상도
w0_range = [-25, 25]
w1_range = [120, 170]
x0 = np.linspace(w0_range[0], w0_range[1], xn)
x1 = np.linspace(w1_range[0], w1_range[1], xn)
xx0, xx1 = np.meshgrid(x0, x1)
J = np.zeros((len(x0), len(x1)))
for i0 in range(xn):
    for i1 in range(xn):
        J[i1, i0] = mse_line(X, T, (x0[i0], x1[i1]))

cont = plt.contour(xx0, xx1, J, 30, colors='black', levels=(100, 1000, 10000, 100000))
cont.clabel(fmt='%1.0f', fontsize=8)
plt.grid(True)

# 구배법 호출
W0, W1, dMSE, W_history = fit_line_num(X, T)

# 결과보기
print('반복 횟수 {0} '.format(W_history.shape[0]))
print('W=[{0:.6f}, {1:.6f}]'.format(W0, W1))
print('dMSE = [{0:.6f}, {1:.6f}]'.format(dMSE[0], dMSE[1]))
print('MSE = {0:.6f}'.format(mse_line(X, T, [W0, W1])))

plt.plot(W_history[:, 0], W_history[:, 1], '.-', color='gray', markersize=10, markeredgecolor='cornflowerblue')

# 제목 추가 (글자 크기 조정)
alpha = 0.00405
plt.title(f'Gradient Descent with Learning Rate = {alpha:.5f}', fontsize=10)

plt.show()
