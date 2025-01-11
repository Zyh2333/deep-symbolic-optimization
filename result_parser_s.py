import csv


def read_and_convert_to_csv(input_file):
    # 准备CSV文件输出
        # 读取输入文件的所有行
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # 读取所有行

        # 遍历每一行并解析内容
        i = 1
        j = 1
        s = []
        print(len(lines))
        lines = lines[1:]
        for line in lines:
            stripped_line = line.strip()

            # 跳过空行
            if not stripped_line:
                continue
            # n = stripped_line.index(" ") + 1
            # stripped_line_back = stripped_line[n:]
            # if stripped_line_back[0] != '0':
            #     idx = stripped_line_back.index('.')
            #     stripped_line_back = stripped_line_back[:idx - 4].replace(" ", '') + stripped_line_back[idx - 4:]
            # stripped_line = stripped_line[:n] + stripped_line_back
            parts = stripped_line.split("_")  # 使用maxsplit限制分割次数
            if str(i) != parts[2] or str(j) != parts[3]:
                print(stripped_line)
                break
            j += 1
            s.append(parts[3])
            if j == 101:
                # print(f"{i}: {s}")
                i = i + 1
                j = 1
                s.clear()

            # if len(parts) != 5:
            #     print(f"警告: 行不符合预期格式 - {stripped_line}")
            #     continue

            identifier, expression, number1, number2, operations = parts


if __name__ == "__main__":
    # input_file = 'dso/log/result.log'  # 输入文件路径
    input_file = 'outputs.csv'  # 输出CSV文件路径

    read_and_convert_to_csv(input_file)
