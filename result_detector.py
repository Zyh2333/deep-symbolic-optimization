import csv


def read_and_convert_to_csv(input_file, output_csv):
    # 准备CSV文件输出
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:

        # 读取输入文件的所有行
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # 读取所有行

            # 遍历每一行并解析内容
            n = 1
            m = 1
            for line in lines:
                stripped_line = line.strip()

                # 跳过空行
                if not stripped_line:
                    continue
                stripped_line = f"sogn_+_{m}_{n}_100 " + stripped_line
                print(stripped_line, file=csvfile)
                n += 1
                if n == 101:
                    n = 1
                    m += 1


if __name__ == "__main__":
    input_file = 'result.log'  # 输入文件路径
    output_csv = 'output.log'  # 输出CSV文件路径

    read_and_convert_to_csv(input_file, output_csv)

    print(f"CSV 文件已创建: {output_csv}")