                except MemoryError:
                    return error_response(u"单个测试数据体积过大!")
                finally:
                    f.close()
            l.sort()

            file_info = {"test_case_number": len(l) / 2, "test_cases": {}}

            # 计算输出文件的md5
            for i in range(len(l) / 2):
                md5 = hashlib.md5()
                striped_md5 = hashlib.md5()
                f = open(test_case_dir + str(i + 1) + ".out", "r")
                # 完整文件的md5
                while True:
                    data = f.read(2 ** 8)
                    if not data:
                        break
                    md5.update(data)
