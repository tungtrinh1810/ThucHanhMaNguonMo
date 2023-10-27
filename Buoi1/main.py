import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog


def get_matrix_input(n):
    matrix = np.zeros((n, n))
    for i in range(n):
        row_input = simpledialog.askstring("Nhập ma trận A",
                                           f"Nhập hàng {i + 1} (cách nhau bởi dấu cách hoặc dấu phẩy):")
        row = [float(x) for x in row_input.split()]
        matrix[i] = row
    return matrix


def get_vector_input(n):
    vector_input = simpledialog.askstring("Nhập vector B", "Nhập vector B (cách nhau bởi dấu cách hoặc dấu phẩy):")
    vector = [float(x) for x in vector_input.split()]
    return vector


def solve_equation():
    n = 0
    while n <= 1:
        try:
            n = int(simpledialog.askstring("Nhập số lượng biến", "Nhập số lượng biến (n > 1):"))
            if n <= 1:
                messagebox.showerror("Lỗi", "Số lượng biến phải lớn hơn 1. Vui lòng nhập lại.")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên lớn hơn 1.")

    A = get_matrix_input(n)
    B = get_vector_input(n)

    try:
        det_A = np.linalg.det(A)

        if det_A == 0:
            messagebox.showinfo("Kết quả", "Hệ phương trình có vô số nghiệm hoặc không có nghiệm.")
        else:
            X = np.linalg.solve(A, B)
            result_str = "Nghiệm của hệ phương trình:\n"
            for i in range(n):
                result_str += f"x{i + 1} = {X[i]}\n"
            messagebox.showinfo("Kết quả", result_str)
    except np.linalg.LinAlgError:
        messagebox.showerror("Lỗi", "Hệ phương trình không có nghiệm hoặc có nghiệm vô số.")
    except ValueError:
        messagebox.showerror("Lỗi", "Lỗi: Hệ phương trình không hợp lệ.")

