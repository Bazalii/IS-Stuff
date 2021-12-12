from math import sqrt, acos, pi
fin = open("input.txt")
fout = open("output.txt", "w")


def Angle_of_shoot(Boat_x, Boat_y, Enemy_x, Enemy_y,Right_side_vector_x, Right_side_vector_y):
    cosinus = (Boat_x * Enemy_x + Boat_y * Enemy_y)/(sqrt(Boat_x ** 2 + Boat_y ** 2) * sqrt(Enemy_x ** 2 + Enemy_y ** 2))
    print(cosinus)
    if cosinus >= 1 or cosinus <= -1:
        return 0, 300
    Angle_of_enemy_relatively_direction = acos(cosinus)*180/pi
    # if ((Right_side_vector_x * Enemy_x + Right_side_vector_y * Enemy_y)/(sqrt(Right_side_vector_x ** 2 + Right_side_vector_y ** 2) * sqrt(Enemy_x ** 2 + Enemy_y ** 2))) >= 1:
    #     return
    Angle_of_enemy_relatively_right_side = acos((Right_side_vector_x * Enemy_x + Right_side_vector_y * Enemy_y)/(sqrt(Right_side_vector_x ** 2 + Right_side_vector_y ** 2) * sqrt(Enemy_x ** 2 + Enemy_y ** 2)))*180/pi
    if Angle_of_enemy_relatively_direction <= 90 and Angle_of_enemy_relatively_right_side <= 90:
        return -1, Angle_of_enemy_relatively_right_side
    elif Angle_of_enemy_relatively_direction <= 90 and Angle_of_enemy_relatively_right_side >= 90:
        return 1, 90 - Angle_of_enemy_relatively_direction
    elif Angle_of_enemy_relatively_direction >= 90 and Angle_of_enemy_relatively_right_side <= 90:
        return -1, -Angle_of_enemy_relatively_right_side
    elif Angle_of_enemy_relatively_direction >= 90 and Angle_of_enemy_relatively_right_side >= 90:
        return 1, -(Angle_of_enemy_relatively_direction - 90)


def Angles_of_mast(M_x, M_y, Right_side_vector_x, Right_side_vector_y):
    Angle_relatively_normal = acos(1/sqrt(M_x ** 2 + M_y ** 2 + 1))*180/pi
    Angle_relatively_right_side = acos((M_x * Right_side_vector_x + M_y * Right_side_vector_y)/(sqrt(M_x ** 2 + M_y ** 2 + 1) * sqrt(Right_side_vector_x ** 2 + Right_side_vector_y ** 2)))*180/pi
    return Angle_relatively_normal, Angle_relatively_right_side


Input_Array = []
Input_Array = fin.readline().split()
V_x, V_y = float(Input_Array[0]), float(Input_Array[1])
Input_Array = fin.readline().split()
Boat_x, Boat_y = float(Input_Array[0]), float(Input_Array[1])
Input_Array = fin.readline().split()
M_x, M_y = float(Input_Array[0]), float(Input_Array[1])
Input_Array = fin.readline().split()
W_x, W_y = float(Input_Array[0]), float(Input_Array[1])
Enemy_x = W_x - V_x
Enemy_y = W_y - V_y
Right_side_vector_x = Boat_y
Right_side_vector_y = -Boat_x
side, Shooting_angle = Angle_of_shoot(Boat_x, Boat_y, Enemy_x, Enemy_y,Right_side_vector_x, Right_side_vector_y)
Angle_of_mast_relatively_normal, Angle_of_mast_relatively_right_side = Angles_of_mast(M_x, M_y, Right_side_vector_x, Right_side_vector_y)
if Shooting_angle < -60 or Shooting_angle > 60 or Angle_of_mast_relatively_normal > 60:
    print(0, file=fout)
    print("Bye, loosers!", file=fout)
else:
    print(side, file=fout)
    print(Shooting_angle, file=fout)
    if (Angle_of_mast_relatively_right_side < 90 and side == -1) or (Angle_of_mast_relatively_right_side > 90 and side == 1):
        Angle_of_mast_relatively_normal *= -1
    print(Angle_of_mast_relatively_normal, file=fout)
    print("Bye, loosers!", file=fout)