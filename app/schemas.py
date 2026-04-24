from pydantic import BaseModel

class InputData(BaseModel):
    Motor_temp: float
    MCU_temp: float
    MCU_Voltage_DC: float
    MCU_AC_Current: float
    Speed: float