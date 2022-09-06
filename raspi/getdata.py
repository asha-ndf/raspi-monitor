
import subprocess
from datetime import datetime

class getD:
    def __init__(self):
        self.debug = 1

    # Commandを実行して結果を返す関数
    def run_shell_command(self,command_str):
        if self.debug ==1:
            return 1
        else:
            proc = subprocess.run(command_str, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            result = proc.stdout.split("=")
        return result[1].replace('\n', '')
    def field_name(self,):
        return ["date","temp","clock","volts","memory_cpu","memory_gpu"]
    def dic(self,):
        date       = datetime.now().strftime("%Y/%m/%d %H:%M:%S")         # 現在時刻
        temp       = self.run_shell_command("vcgencmd measure_temp")      # CPU温度
        clock      = self.run_shell_command("vcgencmd measure_clock arm") # CPU周波数
        volts      = self.run_shell_command("vcgencmd measure_volts")     # CPU電圧
        memory_cpu = self.run_shell_command("vcgencmd get_mem arm")       # CPUのメモリ使用量
        memory_gpu = self.run_shell_command("vcgencmd get_mem gpu")       # GPUのメモリ使用量
        payload = {
            "date" : date,
            "temp" : temp,
            "clock" : clock,
            "volts" : volts,
            "memory_cpu" : memory_cpu,
            "memory_gpu" : memory_gpu
        }
        return payload

if __name__ == "__main__":
    getD = getD()
    field_name = getD.field_name()
    print(field_name)
    payload = getD.dic()
    print(payload)