import ctypes
import os
import time

# DLL Setup
dll_path = r"C:\Users\Desktop\Downloads\ITR-3811 Software Package v1.0.20250515060747886.20250515060747886\ITR-3811_v1.0\Software\RadarAPI\library_v1.155\Windows_mingw_x64\ITR3800_radarAPI.dll"
dll_dir = os.path.dirname(dll_path)
os.environ["PATH"] += ";" + dll_dir

# Load DLL
lib = ctypes.CDLL(dll_path)

# Define ITR3800_getApiVersion

lib.ITR3800_getApiVersion.restype = ctypes.c_int
lib.ITR3800_getApiVersion.argtypes = [ctypes.POINTER(ctypes.c_float)]

version = ctypes.c_float()
ver_res = lib.ITR3800_getApiVersion(ctypes.byref(version))
print("Radar API Version:" if ver_res == 0 else f"Failed to get version. Code: {ver_res}", version.value)

# Define ITR3800_initSystem

lib.ITR3800_initSystem.restype = ctypes.c_int
lib.ITR3800_initSystem.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte]

handle = ctypes.c_void_p()
res = lib.ITR3800_initSystem(ctypes.byref(handle), 192, 168, 31, 69)
print("Connected successfully!" if res == 0 else f"Failed to initialize. Code: {res}")


# Define ITR3800_restartSystem

# lib.ITR3800_restartSystem.restype = ctypes.c_int
# lib.ITR3800_restartSystem.argtypes = [ctypes.c_void_p]

# restart_res = lib.ITR3800_restartSystem(handle)
# if restart_res == 0:
#     print("Device restart initiated successfully. It may take up to 90 seconds.")
# else:
#     print("Failed to restart device. Error code:", restart_res)


# Define System Info Structure

# OUTPUT - Device Information:
#   Product Code     : ITR-3811
#   Serial Number    : 646
#   Software Version : 1.013

# class ITR3800_SystemInfo_t(ctypes.Structure):
#     _fields_ = [
#         ("productcode", ctypes.c_int),
#         ("serialNumber", ctypes.c_int),
#         ("swVersionMajor", ctypes.c_int),
#         ("swVersionMinor", ctypes.c_int)
#     ]

# # Define ITR3800_getSystemInfo

# lib.ITR3800_getSystemInfo.restype = ctypes.c_int
# lib.ITR3800_getSystemInfo.argtypes = [ctypes.c_void_p, ctypes.POINTER(ITR3800_SystemInfo_t)]

# info = ITR3800_SystemInfo_t()
# info_res = lib.ITR3800_getSystemInfo(handle, ctypes.byref(info))
# if info_res == 0:
#     print("Device Information:")
#     print(f"  Product Code     : ITR-{info.productcode}")
#     print(f"  Serial Number    : {info.serialNumber}")
#     print(f"  Software Version : {info.swVersionMajor}.{info.swVersionMinor:03}")
# else:
#     print("Failed to retrieve system info. Error code:", info_res)


# # Define GetsystemInfo

# class ITR3800_Description_t(ctypes.Structure):
#     _fields_ = [
#         ("description", ctypes.c_char * 128),
#         ("descriptionLength", ctypes.c_uint32),
#     ]

# # Define ITR3800_setDescription
# lib.ITR3800_setDescription.restype = ctypes.c_int
# lib.ITR3800_setDescription.argtypes = [ctypes.c_void_p, ITR3800_Description_t]

# # Define ITR3800_getDescription
# lib.ITR3800_getDescription.restype = ctypes.c_int
# lib.ITR3800_getDescription.argtypes = [ctypes.c_void_p, ctypes.POINTER(ITR3800_Description_t)]

# # -------- SET DESCRIPTION --------
# desc_text = "this is my device"
# desc_struct = ITR3800_Description_t()
# desc_struct.description = desc_text.encode('utf-8')
# desc_struct.descriptionLength = len(desc_text)

# set_res = lib.ITR3800_setDescription(handle, desc_struct)
# if set_res == 0:
#     print("Description set successfully!")
# else:
#     print("Failed to set description. Error code:", set_res)

# # -------- GET DESCRIPTION --------

# get_desc_struct = ITR3800_Description_t()
# get_res = lib.ITR3800_getDescription(handle, ctypes.byref(get_desc_struct))
# if get_res == 0:
#     device_description = get_desc_struct.description[:get_desc_struct.descriptionLength].decode('utf-8')
#     print("Device Description:", device_description)
# else:
#     print("Failed to get description. Error code:", get_res)

# # Define setUdpSettings

# lib.ITR3800_setUdpSettings.restype = ctypes.c_int
# lib.ITR3800_setUdpSettings.argtypes = [
#     ctypes.c_void_p,     # handle
#     ctypes.c_uint32,     # mode (assuming enum is uint32_t or similar)
#     ctypes.c_uint16,     # port
#     ctypes.c_ubyte,      # ip1
#     ctypes.c_ubyte,      # ip2
#     ctypes.c_ubyte,      # ip3
#     ctypes.c_ubyte       # ip4
# ]

# lib.ITR3800_getUdpSettings.restype = ctypes.c_int
# lib.ITR3800_getUdpSettings.argtypes = [
#     ctypes.c_void_p,                         # handle
#     ctypes.POINTER(ctypes.c_uint32),        # mode
#     ctypes.POINTER(ctypes.c_uint16),        # port
#     ctypes.POINTER(ctypes.c_ubyte),         # ip1
#     ctypes.POINTER(ctypes.c_ubyte),         # ip2
#     ctypes.POINTER(ctypes.c_ubyte),         # ip3
#     ctypes.POINTER(ctypes.c_ubyte)          # ip4
# ]


# ITR3800_UDP_MODE_BROADCAST = 0 

# udp_res = lib.ITR3800_setUdpSettings(handle, ITR3800_UDP_MODE_BROADCAST, 62200, 192, 168, 31, 122)
# if udp_res == 0:
#     print("UDP settings set successfully!")
# else:
#     print("Failed to set UDP settings. Error code:", udp_res)

# mode = ctypes.c_uint32()
# port = ctypes.c_uint16()
# ip1 = ctypes.c_ubyte()
# ip2 = ctypes.c_ubyte()
# ip3 = ctypes.c_ubyte()
# ip4 = ctypes.c_ubyte()

# get_udp_res = lib.ITR3800_getUdpSettings(handle,
#                                          ctypes.byref(mode),
#                                          ctypes.byref(port),
#                                          ctypes.byref(ip1),
#                                          ctypes.byref(ip2),
#                                          ctypes.byref(ip3),
#                                          ctypes.byref(ip4))

# if get_udp_res == 0:
#     print("UDP Settings:")
#     print("  Mode       :", mode.value)
#     print("  Port       :", port.value)
#     print("  IP Address :", f"{ip1.value}.{ip2.value}.{ip3.value}.{ip4.value}")
# else:
#     print("Failed to get UDP settings. Error code:", get_udp_res)


# #------Define types for Static Ip


# # APIHandle_t = ctypes.c_void_p  
# # ITR3800_Result_t = ctypes.c_int  

# # # Set function prototype
# # lib.ITR3800_setStaticIP.restype = ITR3800_Result_t
# # lib.ITR3800_setStaticIP.argtypes = [
# #     APIHandle_t,
# #     ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte,  # IP address
# #     ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte,  # Subnet mask
# #     ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte   # Gateway
# # ]

# # # Call the function
# # res = lib.ITR3800_setStaticIP(
# #     handle,
# #     192, 168, 31, 69,        # Static IP
# #     255, 255, 255, 0,          # Subnet Mask
# #     192, 168, 31, 1,          # Gateway
# # )

# # # Check result
# # ITR3800_API_ERR_OK = 0  
# # if res != ITR3800_API_ERR_OK:
# #     print(f"Error – ITR3800_setStaticIP failed. Error code: {res}")
# # else:
# #     print("Static IP set successfully")\
    


# # ------------Set function DHCP

# # APIHandle_t = ctypes.c_void_p
# # ITR3800_Result_t = ctypes.c_int

# # lib.ITR3800_setDhcpIP.restype = ITR3800_Result_t
# # lib.ITR3800_setDhcpIP.argtypes = [APIHandle_t]

# # # Call the function
# # res = lib.ITR3800_setDhcpIP(handle)

# # # Check result
# # if res != ITR3800_Result_t:
# #     print(f"Error – ITR3800_setDhcpIP failed. Error code: {res}")
# # else:
# #     print("DHCP enabled successfully")

 
# #----------- define set/getNetworkHostname

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
 
# lib.ITR3800_setNetworkHostname.restype = ITR3800_Result_t
# lib.ITR3800_setNetworkHostname.argtypes = [APIHandle_t, ctypes.POINTER(ctypes.c_char), ctypes.c_uint8]

# lib.ITR3800_getNetworkHostname.restype = ITR3800_Result_t
# lib.ITR3800_getNetworkHostname.argtypes = [APIHandle_t, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_uint8)]

# # Set hostname
# hostname = b"MyRadar001"
# hostname_length = len(hostname)
# hostname_buffer = (ctypes.c_char * 255)()
# ctypes.memmove(hostname_buffer, hostname, hostname_length)

# res = lib.ITR3800_setNetworkHostname(handle, hostname_buffer, hostname_length)
# print("Set result:", res)

# # Get hostname
# get_buffer = (ctypes.c_char * 255)()
# length = ctypes.c_uint8()
# res = lib.ITR3800_getNetworkHostname(handle, get_buffer, ctypes.byref(length))

# if res == 0:
#     print("Hostname:", get_buffer[:length.value].decode('utf-8'))
# else:
#     print("Failed to get hostname. Code:", res)


# #-------- set/getInstallationHeight

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# float32_t = ctypes.c_float

# lib.ITR3800_setInstallationHeight.restype = ITR3800_Result_t
# lib.ITR3800_setInstallationHeight.argtypes = [APIHandle_t, float32_t]

# lib.ITR3800_getInstallationHeight.restype = ITR3800_Result_t
# lib.ITR3800_getInstallationHeight.argtypes = [APIHandle_t, ctypes.POINTER(float32_t)]

# # SET INSTALLATION HEIGHT
# set_height = float32_t(6.0)
# res = lib.ITR3800_setInstallationHeight(handle, set_height)
# if res != 0:
#     print("Error – ITR3800_setInstallationHeight failed")
# else:
#     print("Installation height set successfully.")

# # GET INSTALLATION HEIGHT
# height = float32_t()
# res = lib.ITR3800_getInstallationHeight(handle, ctypes.byref(height))
# if res != 0:
#     print("Error – ITR3800_getInstallationHeight failed")
# else:
#     print(f"Installation height: {height.value:.2f} m") 



# #-------- set/getElevationAngle


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# float32_t = ctypes.c_float

# # Declare function signatures
# lib.ITR3800_setElevationAngle.restype = ITR3800_Result_t
# lib.ITR3800_setElevationAngle.argtypes = [APIHandle_t, float32_t]

# lib.ITR3800_getElevationAngle.restype = ITR3800_Result_t
# lib.ITR3800_getElevationAngle.argtypes = [APIHandle_t, ctypes.POINTER(float32_t)]

# # SET ELEVATION ANGLE
# elevation_angle = float32_t(-7.0)
# res = lib.ITR3800_setElevationAngle(handle, elevation_angle)
# if res != 0:
#     print("Error – ITR3800_setElevationAngle failed")
# else:
#     print("Elevation angle set successfully.")

# # GET ELEVATION ANGLE
# angle = float32_t()
# res = lib.ITR3800_getElevationAngle(handle, ctypes.byref(angle))
# if res != 0:
#     print("Error – ITR3800_getElevationAngle failed")
# else:
#     print(f"Elevation angle: {angle.value:.2f} deg")   



# #----------- define getInclinationAngles


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# float32_t = ctypes.c_float

# # Declare the function signature
# lib.ITR3800_getInclinationAngles.restype = ITR3800_Result_t
# lib.ITR3800_getInclinationAngles.argtypes = [APIHandle_t, ctypes.POINTER(float32_t), ctypes.POINTER(float32_t)]

# # Prepare variables
# pitch = float32_t()
# roll = float32_t()

# # Call the function
# res = lib.ITR3800_getInclinationAngles(handle, ctypes.byref(pitch), ctypes.byref(roll))

# # Check result
# if res != 0:
#     print("Error – ITR3800_getInclinationAngles failed")
# else:
#     print(f"Inclination - Pitch: {pitch.value:.1f} deg, Roll: {roll.value:.1f} deg")


# #------------- def DateTime

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# uint16_t = ctypes.c_uint16
# uint8_t = ctypes.c_uint8
# ITR3800_TimeZone_t = ctypes.c_int  # Assuming enum is mapped to int in C

# # Replace with the actual constant from your header (value for Berlin/Amsterdam timezone)
# ITR3800_API_TIMEZONE_AMSTERDAM_BERLIN_ROME_STOCKHOLM_VIENNA = 1

# # Declare function prototypes
# lib.ITR3800_setDateTime.restype = ITR3800_Result_t
# lib.ITR3800_setDateTime.argtypes = [
#     APIHandle_t, uint16_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, ITR3800_TimeZone_t
# ]

# lib.ITR3800_getDateTime.restype = ITR3800_Result_t
# lib.ITR3800_getDateTime.argtypes = [
#     APIHandle_t,
#     ctypes.POINTER(uint16_t), ctypes.POINTER(uint8_t), ctypes.POINTER(uint8_t),
#     ctypes.POINTER(uint8_t), ctypes.POINTER(uint8_t), ctypes.POINTER(uint8_t),
#     ctypes.POINTER(ITR3800_TimeZone_t)
# ]


# res = lib.ITR3800_setDateTime(
#     handle,
#     uint16_t(2019), uint8_t(9), uint8_t(21),
#     uint8_t(7), uint8_t(8), uint8_t(9),
#     ITR3800_TimeZone_t(ITR3800_API_TIMEZONE_AMSTERDAM_BERLIN_ROME_STOCKHOLM_VIENNA)
# )

# if res != 0:
#     print("Error – ITR3800_setDateTime failed")
# else:
#     print("Date and time set successfully.")


# year = uint16_t()
# month = uint8_t()
# day = uint8_t()
# hour = uint8_t()
# minute = uint8_t()
# second = uint8_t()
# timezone = ITR3800_TimeZone_t()

# res = lib.ITR3800_getDateTime(
#     handle,
#     ctypes.byref(year), ctypes.byref(month), ctypes.byref(day),
#     ctypes.byref(hour), ctypes.byref(minute), ctypes.byref(second),
#     ctypes.byref(timezone)
# )

# if res != 0:
#     print("Error – ITR3800_getDateTime failed")
# else:
#     print(f"Date: {year.value}-{month.value}-{day.value}")
#     print(f"Time: {hour.value}:{minute.value}:{second.value}")
#     print(f"Timezone (enum value): {timezone.value}")   


# # ---------define set/getGpsDateTimeSyncEnable 


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# bool_t = ctypes.c_bool 


# lib.ITR3800_setGpsDateTimeSyncEnable.restype = ITR3800_Result_t
# lib.ITR3800_setGpsDateTimeSyncEnable.argtypes = [APIHandle_t, bool_t]

# lib.ITR3800_getGpsDateTimeSyncEnable.restype = ITR3800_Result_t
# lib.ITR3800_getGpsDateTimeSyncEnable.argtypes = [APIHandle_t, ctypes.POINTER(bool_t)]

# # ----- SET GPS SYNCHRONIZATION ENABLE -----
# res = lib.ITR3800_setGpsDateTimeSyncEnable(handle, bool_t(False))
# if res != 0:
#     print("Error – ITR3800_setGpsDateTimeSyncEnable failed")
# else:
#     print("GPS synchronization disable command sent successfully.")

# # ----- GET GPS SYNCHRONIZATION ENABLE -----
# gps_enable = bool_t()
# res = lib.ITR3800_getGpsDateTimeSyncEnable(handle, ctypes.byref(gps_enable))
# if res != 0:
#     print("Error – ITR3800_getGpsDateTimeSyncEnable failed")
# else:
#     print(f"GPS synchronization enable: {int(gps_enable.value)}")


# #--------------- def set/getNtpDateTimeSyncEnable 


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# bool_t = ctypes.c_bool  

# # Declare function prototypes
# lib.ITR3800_setNtpDateTimeSyncEnable.restype = ITR3800_Result_t
# lib.ITR3800_setNtpDateTimeSyncEnable.argtypes = [APIHandle_t, bool_t]

# lib.ITR3800_getNtpDateTimeSyncEnable.restype = ITR3800_Result_t
# lib.ITR3800_getNtpDateTimeSyncEnable.argtypes = [APIHandle_t, ctypes.POINTER(bool_t)]

# # ----- SET NTP SYNCHRONIZATION ENABLE -----
# res = lib.ITR3800_setNtpDateTimeSyncEnable(handle, bool_t(False))
# if res != 0:
#     print("Error – ITR3800_setNtpDateTimeSyncEnable failed")
# else:
#     print("NTP synchronization disabled successfully.")

# # ----- GET NTP SYNCHRONIZATION ENABLE -----
# ntp_enable = bool_t()
# res = lib.ITR3800_getNtpDateTimeSyncEnable(handle, ctypes.byref(ntp_enable))
# if res != 0:
#     print("Error – ITR3800_getNtpDateTimeSyncEnable failed")
# else:
#     print(f"NTP synchronization enable: {int(ntp_enable.value)}")   


# # ------------------- def set/getPreferredNtpServer

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# uint8_t = ctypes.c_uint8

# # Declare function prototypes
# lib.ITR3800_setPreferredNtpServer.restype = ITR3800_Result_t
# lib.ITR3800_setPreferredNtpServer.argtypes = [APIHandle_t, ctypes.POINTER(ctypes.c_char), uint8_t]

# lib.ITR3800_getPreferredNtpServer.restype = ITR3800_Result_t
# lib.ITR3800_getPreferredNtpServer.argtypes = [APIHandle_t, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(uint8_t)]

# # ----- SET NTP SERVER -----
# ntp_server = b"0.arch.pool.ntp.org"
# ntp_length = len(ntp_server)
# ntp_buffer = (ctypes.c_char * 255)()
# ctypes.memmove(ntp_buffer, ntp_server, ntp_length)

# res = lib.ITR3800_setPreferredNtpServer(handle, ntp_buffer, uint8_t(ntp_length))
# if res != 0:
#     print("Error – ITR3800_setPreferredNtpServer failed")
# else:
#     print("NTP server set successfully.")

# # ----- GET NTP SERVER -----
# ntp_read_buffer = (ctypes.c_char * 255)()
# length = uint8_t()

# res = lib.ITR3800_getPreferredNtpServer(handle, ntp_read_buffer, ctypes.byref(length))
# if res != 0:
#     print("Error – ITR3800_getPreferredNtpServer failed")
# else:
#     ntp_server_str = ntp_read_buffer[:length.value].decode('utf-8')
#     print(f"NTP server: {ntp_server_str}")  


# # --------------def set/getHeartbeatMessageEnable 

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# bool_t = ctypes.c_bool  # Use c_uint8 if bool_t is not standard C bool

# # Declare function prototypes
# lib.ITR3800_setHeartbeatMessageEnable.restype = ITR3800_Result_t
# lib.ITR3800_setHeartbeatMessageEnable.argtypes = [APIHandle_t, bool_t]

# lib.ITR3800_getHeartbeatMessageEnable.restype = ITR3800_Result_t
# lib.ITR3800_getHeartbeatMessageEnable.argtypes = [APIHandle_t, ctypes.POINTER(bool_t)]

# # ----- SET HEARTBEAT ENABLE -----
# res = lib.ITR3800_setHeartbeatMessageEnable(handle, bool_t(False))
# if res != 0:
#     print("Error – ITR3800_setHeartbeatMessageEnable failed")
# else:
#     print("Heartbeat message disabled successfully.")

# # ----- GET HEARTBEAT ENABLE -----
# heartbeat_enable = bool_t()
# res = lib.ITR3800_getHeartbeatMessageEnable(handle, ctypes.byref(heartbeat_enable))
# if res != 0:
#     print("Error – ITR3800_getHeartbeatMessageEnable failed")
# else:
#     print(f"Heartbeat message enable: {int(heartbeat_enable.value)}")    


# # --------------def getGpsCoordinates

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# float32_t = ctypes.c_float

# # Declare function prototype
# lib.ITR3800_getGpsCoordinates.restype = ITR3800_Result_t
# lib.ITR3800_getGpsCoordinates.argtypes = [APIHandle_t, ctypes.POINTER(float32_t), ctypes.POINTER(float32_t)]

# # ----- GET GPS COORDINATES -----
# latitude = float32_t()
# longitude = float32_t()

# res = lib.ITR3800_getGpsCoordinates(handle, ctypes.byref(latitude), ctypes.byref(longitude))

# if res != 0:
#     print("Error – ITR3800_getGpsCoordinates failed")
# elif latitude.value == 0.0 and longitude.value == 0.0:
#     print("GPS location: no signal")
# else:
#     print(f"GPS location latitude : {latitude.value:.5f} deg")
#     print(f"GPS location longitude: {longitude.value:.5f} deg")     



# #---------- def set/getFrequencyChannel


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# ITR3800_FrequencyChannel_t = ctypes.c_int  # Assuming it's an enum in C

# # Replace with the actual constant from your header file
# ITR3800_FREQUENCY_CHANNEL_1 = 1

# # Declare function prototypes
# lib.ITR3800_setFrequencyChannel.restype = ITR3800_Result_t
# lib.ITR3800_setFrequencyChannel.argtypes = [APIHandle_t, ITR3800_FrequencyChannel_t]

# lib.ITR3800_getFrequencyChannel.restype = ITR3800_Result_t
# lib.ITR3800_getFrequencyChannel.argtypes = [APIHandle_t, ctypes.POINTER(ITR3800_FrequencyChannel_t)]

# # ----- SET FREQUENCY CHANNEL -----
# res = lib.ITR3800_setFrequencyChannel(handle, ITR3800_FrequencyChannel_t(ITR3800_FREQUENCY_CHANNEL_1))
# if res != 0:
#     print("Error – ITR3800_setFrequencyChannel failed")
# else:
#     print("Frequency channel set successfully.")

# # ----- GET FREQUENCY CHANNEL -----
# channel = ITR3800_FrequencyChannel_t()
# res = lib.ITR3800_getFrequencyChannel(handle, ctypes.byref(channel))

# if res != 0:
#     print("Error – ITR3800_getFrequencyChannel failed")
# else:
#     print(f"Frequency channel: {channel.value}")    


# ------------- def set/getRainInterferenceLevelThreshold

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# float32_t = ctypes.c_float

# # Declare function prototypes
# lib.ITR3800_setRainInterferenceLevelThreshold.restype = ITR3800_Result_t
# lib.ITR3800_setRainInterferenceLevelThreshold.argtypes = [APIHandle_t, float32_t]

# lib.ITR3800_getRainInterferenceLevelThreshold.restype = ITR3800_Result_t
# lib.ITR3800_getRainInterferenceLevelThreshold.argtypes = [APIHandle_t, ctypes.POINTER(float32_t)]

# # ----- SET RAIN INTERFERENCE LEVEL THRESHOLD -----
# res = lib.ITR3800_setRainInterferenceLevelThreshold(handle, float32_t(30.0))
# if res != 0:
#     print("Error – ITR3800_setRainInterferenceLevelThreshold failed")
# else:
#     print("Rain interference level threshold set successfully.")

# # ----- GET RAIN INTERFERENCE LEVEL THRESHOLD -----
# threshold_dB = float32_t()
# res = lib.ITR3800_getRainInterferenceLevelThreshold(handle, ctypes.byref(threshold_dB))

# if res != 0:
#     print("Error – ITR3800_getRainInterferenceLevelThreshold failed")
# else:
#     print(f"Rain interference level threshold: {threshold_dB.value:.2f} dB")    


#----------------def set/getSimulation


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# float32_t = ctypes.c_float

# # Declare function prototypes
# lib.ITR3800_setSimulation.restype = ITR3800_Result_t
# lib.ITR3800_setSimulation.argtypes = [APIHandle_t, ctypes.c_int]  # enable/disable is an int

# lib.ITR3800_getSimulation.restype = ITR3800_Result_t
# lib.ITR3800_getSimulation.argtypes = [APIHandle_t, ctypes.POINTER(float32_t)]

# # ----- SET SIMULATION MODE -----
# res = lib.ITR3800_setSimulation(handle, 1)
# if res != 0:
#     print("Error – ITR3800_setSimulation failed")
# else:
#     print("Simulation mode enabled successfully.")

# # ----- GET SIMULATION MODE STATUS -----
# enable = float32_t()
# res = lib.ITR3800_getSimulation(handle, ctypes.byref(enable))

# if res != 0:
#     print("Error – ITR3800_getSimulation failed")
# else:
#     print(f"Simulation mode: {int(enable.value)}")
 

# -------------def set/getUnitTypes

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# ITR3800_UnitType_t = ctypes.c_int  # Enum in C

# # === Define Enum Constants (replace with actual values from your header) ===
# ITR3800_UNIT_METER = 0     # Replace with real value if different
# ITR3800_UNIT_KMH = 1       # Replace with real value if different

# # === Declare Function Prototypes ===
# lib.ITR3800_setUnitTypes.restype = ITR3800_Result_t
# lib.ITR3800_setUnitTypes.argtypes = [APIHandle_t, ITR3800_UnitType_t, ITR3800_UnitType_t]

# lib.ITR3800_getUnitTypes.restype = ITR3800_Result_t
# lib.ITR3800_getUnitTypes.argtypes = [APIHandle_t, ctypes.POINTER(ITR3800_UnitType_t), ctypes.POINTER(ITR3800_UnitType_t)]

# # === SET UNIT TYPES ===
# res = lib.ITR3800_setUnitTypes(handle, ITR3800_UNIT_METER, ITR3800_UNIT_KMH)
# if res != 0:
#     print("Error – ITR3800_setUnitTypes failed")
# else:
#     print("Unit types set successfully.")

# === GET UNIT TYPES ===
# distance_unit = ITR3800_UnitType_t()
# velocity_unit = ITR3800_UnitType_t()

# res = lib.ITR3800_getUnitTypes(handle, ctypes.byref(distance_unit), ctypes.byref(velocity_unit))
# if res != 0:
#     print("Error – ITR3800_getUnitTypes failed")
# else:
#     print(f"Distance unit: {distance_unit.value}")
#     print(f"Velocity unit: {velocity_unit.value}") 


# ----------------def set/getStaticTargetsEnable


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# uint8_t = ctypes.c_uint8  # Equivalent to uint8_t in C

# # === Declare Function Prototypes ===
# lib.ITR3800_setStaticTargetsEnable.restype = ITR3800_Result_t
# lib.ITR3800_setStaticTargetsEnable.argtypes = [APIHandle_t, ctypes.c_int]  # 1 = enable, 0 = disable

# lib.ITR3800_getStaticTargetsEnable.restype = ITR3800_Result_t
# lib.ITR3800_getStaticTargetsEnable.argtypes = [APIHandle_t, ctypes.POINTER(uint8_t)]

# # === SET STATIC TARGETS ENABLE ===
# res = lib.ITR3800_setStaticTargetsEnable(handle, 1)
# if res != 0:
#     print("Error – ITR3800_setStaticTargetsEnable failed")
# else:
#     print("Static targets enabled successfully.")

# # === GET STATIC TARGETS ENABLE STATUS ===
# enable = uint8_t()
# res = lib.ITR3800_getStaticTargetsEnable(handle, ctypes.byref(enable))

# if res != 0:
#     print("Error – ITR3800_getStaticTargetsEnable failed")
# else:
#     print(f"Static targets enabled status: {enable.value}")   


# # -------------def set/getHighwayMode

# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# uint8_t = ctypes.c_uint8  # Equivalent to uint8_t in C

# # === Declare Function Prototypes ===
# lib.ITR3800_setHighwayMode.restype = ITR3800_Result_t
# lib.ITR3800_setHighwayMode.argtypes = [APIHandle_t, ctypes.c_int]  # 1 = enable, 0 = disable

# lib.ITR3800_getHighwayMode.restype = ITR3800_Result_t
# lib.ITR3800_getHighwayMode.argtypes = [APIHandle_t, ctypes.POINTER(uint8_t)]

# # === ENABLE HIGHWAY MODE ===
# res = lib.ITR3800_setHighwayMode(handle, 1)
# if res != 0:
#     print("Error – ITR3800_setHighwayMode failed")
# else:
#     print("Highway mode enabled successfully.")

# # === GET HIGHWAY MODE STATUS ===
# enable = uint8_t()
# res = lib.ITR3800_getHighwayMode(handle, ctypes.byref(enable))
# if res != 0:
#     print("Error – ITR3800_getHighwayMode failed")
# else:
#     print(f"Highway mode: {enable.value}") 



# # ---------def   set/getMaxStopTimeObject


# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# uint16_t = ctypes.c_uint16  # Equivalent to uint16_t in C

# # === Declare Function Prototypes ===
# lib.ITR3800_setMaxStopTimeObject.restype = ITR3800_Result_t
# lib.ITR3800_setMaxStopTimeObject.argtypes = [APIHandle_t, ctypes.c_uint16]  # 300 seconds

# lib.ITR3800_getMaxStopTimeObject.restype = ITR3800_Result_t
# lib.ITR3800_getMaxStopTimeObject.argtypes = [APIHandle_t, ctypes.POINTER(uint16_t)]

# # === SET MAX STOP TIME FOR STATIC OBJECTS ===
# res = lib.ITR3800_setMaxStopTimeObject(handle, 300)  # in seconds
# if res != 0:
#     print("Error – ITR3800_setMaxStopTimeObject failed")
# else:
#     print("Max stop time for static objects set successfully.")

# # === GET MAX STOP TIME FOR STATIC OBJECTS ===
# time_s = uint16_t()
# res = lib.ITR3800_getMaxStopTimeObject(handle, ctypes.byref(time_s))
# if res != 0:
#     print("Error – ITR3800_getMaxStopTimeObject failed")
# else:
#     print(f"Max stop time for static objects: {time_s.value} seconds")    


#----def getobject---------


# Type definitions
APIHandle_t = ctypes.c_void_p
ITR3800_Result_t = ctypes.c_int
uint16_t = ctypes.c_uint16
uint32_t = ctypes.c_uint32

# Constants (adjust based on your API documentation)
MAX_OBJECTS = 100  # Adjust this based on your system's maximum tracked objects
ITR3800_API_ERR_OK = 0

# SAFE VERSION - Start with minimal structure to avoid segfault
class ITR3800_ObjectList_t(ctypes.Structure):
    _fields_ = [
        ("nrOfTracks", uint16_t),
        # Don't include object array initially - just get count first
    ]

# Alternative: Define object structure but don't use array yet
class ITR3800_Object_t(ctypes.Structure):
    _fields_ = [
        ("id", uint16_t),           # Object ID
        ("x", ctypes.c_float),      # X position
        ("y", ctypes.c_float),      # Y position  
        ("vx", ctypes.c_float),     # X velocity
        ("vy", ctypes.c_float),     # Y velocity
        ("range", ctypes.c_float),  # Distance from sensor
        ("angle", ctypes.c_float),  # Angle from sensor
    ]

def setup_object_tracking(lib, handle):
    """Setup the object tracking function prototypes"""
    # Declare function prototype
    lib.ITR3800_getObjectList.restype = ITR3800_Result_t
    lib.ITR3800_getObjectList.argtypes = [APIHandle_t, ctypes.POINTER(ITR3800_ObjectList_t)]

def get_object_list_single(lib, handle):
    """Get object list once"""
    object_list = ITR3800_ObjectList_t()
    res = lib.ITR3800_getObjectList(handle, ctypes.byref(object_list))
    
    if res != ITR3800_API_ERR_OK:
        print(f"Error – ITR3800_getObjectList failed with code: {res}")
        return None, res
    else:
        print(f"Number of objects: {object_list.nrOfTracks}")
        return object_list, res

def display_object_details(object_list):
    """Display detailed information about tracked objects"""
    if object_list.nrOfTracks > 0:
        print("\n--- Tracked Objects ---")
        for i in range(object_list.nrOfTracks):
            obj = object_list.objects[i]
            print(f"Object {i+1}:")
            print(f"  ID: {obj.id}")
            print(f"  Position: ({obj.x:.2f}, {obj.y:.2f})")
            print(f"  Velocity: ({obj.vx:.2f}, {obj.vy:.2f})")
            print(f"  Range: {obj.range:.2f}")
            print(f"  Angle: {obj.angle:.2f}°")
            print(f"  RCS: {obj.rcs:.2f}")
            print(f"  Timestamp: {obj.timestamp}")
            print()
    else:
        print("No active objects being tracked")

def continuous_object_tracking(lib, handle, duration_seconds=10, update_interval=0.1):
    """Continuously track objects for a specified duration"""
    print(f"Starting continuous object tracking for {duration_seconds} seconds...")
    print("Press Ctrl+C to stop early\n")
    
    start_time = time.time()
    iteration = 0
    
    try:
        while (time.time() - start_time) < duration_seconds:
            iteration += 1
            print(f"\n--- Update {iteration} (Time: {time.time() - start_time:.1f}s) ---")
            
            object_list, res = get_object_list_single(lib, handle)
            
            if object_list is not None:
                display_object_details(object_list)
            
            time.sleep(update_interval)
            
    except KeyboardInterrupt:
        print("\nTracking stopped by user")
    
    print(f"\nTracking completed after {iteration} updates")

# Main execution example
def main_tracking_example(lib, handle):
    """Main function to demonstrate object tracking"""
    
    # Setup function prototypes
    setup_object_tracking(lib, handle)
    
    print("ITR3800 Object Tracking Started")
    print("================================")
    
    # Test single call first
    print("\n1. Testing single object list call...")
    object_list, res = get_object_list_single(lib, handle)
    
    if object_list is not None:
        display_object_details(object_list)
    
    # Ask user if they want continuous tracking
    print("\n2. Starting continuous tracking...")
    continuous_object_tracking(lib, handle, duration_seconds=300, update_interval=0.1)

# Usage example (uncomment and modify as needed):
# 
# Assuming you have already loaded your library and have a handle:
# lib = ctypes.CDLL("your_itr3800_library.dll")  # or .so on Linux
# handle = your_handle_initialization_code
# 
# # Run the tracking
main_tracking_example(lib, handle)

# Alternative: Simple loop for testing
def simple_tracking_loop(lib, handle, num_iterations=50):
    """Simple tracking loop for basic testing"""
    setup_object_tracking(lib, handle)
    
    print("Running simple tracking loop...")
    for i in range(num_iterations):
        print(f"\n--- Iteration {i+1}/{num_iterations} ---")
        object_list, res = get_object_list_single(lib, handle)
        
        if object_list is not None and object_list.nrOfTracks > 0:
            print(f"Found {object_list.nrOfTracks} active objects")
            # Display first object details as example
            if object_list.nrOfTracks > 0:
                obj = object_list.objects[0]
                print(f"First object - ID: {obj.id}, Pos: ({obj.x:.2f}, {obj.y:.2f}), Vel: ({obj.vx:.2f}, {obj.vy:.2f})")
        
        time.sleep(0.085)  # Wait ~85ms (matching the update rate)

# Troubleshooting function
def debug_tracking_setup(lib, handle):
    """Debug function to help identify issues"""
    print("Debugging ITR3800 Object Tracking Setup")
    print("=====================================")
    
    # Test if function exists
    try:
        func = lib.ITR3800_getObjectList
        print("✓ ITR3800_getObjectList function found in library")
    except AttributeError:
        print("✗ ITR3800_getObjectList function NOT found in library")
        return
    
    # Test handle validity
    if handle is None or handle == 0:
        print("✗ Handle appears to be invalid (None or 0)")
        return
    else:
        print(f"✓ Handle appears valid: {handle}")
    
    # Test structure size
    obj_size = ctypes.sizeof(ITR3800_Object_t)
    list_size = ctypes.sizeof(ITR3800_ObjectList_t)
    print(f"✓ Object structure size: {obj_size} bytes")
    print(f"✓ Object list structure size: {list_size} bytes")
    
    # Try a single call
    print("\nTesting single function call...")
    setup_object_tracking(lib, handle)
    object_list, res = get_object_list_single(lib, handle)
    
    if res == ITR3800_API_ERR_OK:
        print("✓ Function call successful")
    else:
        print(f"✗ Function call failed with code: {res}")

# Assuming previous typedefs:
# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# uint16_t = ctypes.c_uint16

# # Define Object List structure
# class ITR3800_ObjectList_t(ctypes.Structure):
#     _fields_ = [
#         ("nrOfTracks", uint16_t),

#     ]

# # Declare function prototype
# lib.ITR3800_getObjectList.restype = ITR3800_Result_t
# lib.ITR3800_getObjectList.argtypes = [APIHandle_t, ctypes.POINTER(ITR3800_ObjectList_t)]

# # Call function
# object_list = ITR3800_ObjectList_t()
# res = lib.ITR3800_getObjectList(handle, ctypes.byref(object_list))
# if res != 0:
#     print("Error – ITR3800_getObjectList failed")
# else:
#     print(f"Number of objects: {object_list.nrOfTracks}")

#-----------def removeObject

# lib.ITR3800_removeObject.restype = ITR3800_Result_t
# lib.ITR3800_removeObject.argtypes = [APIHandle_t, ctypes.c_uint16]

# object_id = 21  
# res = lib.ITR3800_removeObject(handle, object_id)

# if res != 0: 
#     print("Error – ITR3800_removeObject failed")
# else:
#     print(f"Object with ID {object_id} removed successfully.")


# === Constants (adjust according to your SDK) ===
# ITR3800_EVENTZONE_PRESENSE = 1
# ITR3800_MAX_NR_OF_EVENTZONES = 8
# ITR3800_MAX_NR_OF_ZONE_POINTS = 4

# # === Type Definitions ===
# APIHandle_t = ctypes.c_void_p
# ITR3800_Result_t = ctypes.c_int
# uint16_t = ctypes.c_uint16
# bool_t = ctypes.c_bool  # If your SDK uses uint8_t for bool, replace with ctypes.c_uint8

# # === Structures ===

# class ZoneDataPoint(ctypes.Structure):
#     _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float)]

# class EventZone(ctypes.Structure):
#     _fields_ = [
#         ("enable", bool_t),
#         ("zoneType", ctypes.c_uint8),
#         ("nrOfZonePoints", ctypes.c_uint8),
#         ("zoneData", ZoneDataPoint * ITR3800_MAX_NR_OF_ZONE_POINTS)
#     ]

# class ITR3800_EventZones_t(ctypes.Structure):
#     _fields_ = [("eventZones", EventZone * ITR3800_MAX_NR_OF_EVENTZONES)]

# === Function Prototypes ===

# lib.ITR3800_setEventZones.restype = ITR3800_Result_t
# lib.ITR3800_setEventZones.argtypes = [APIHandle_t, ITR3800_EventZones_t]

# lib.ITR3800_getEventZones.restype = ITR3800_Result_t
# lib.ITR3800_getEventZones.argtypes = [APIHandle_t, ctypes.POINTER(ITR3800_EventZones_t)]

# === SET EVENT ZONE ===

# event = ITR3800_EventZones_t()
# zone = event.eventZones[0]

# zone.enable = True
# zone.zoneType = ITR3800_EVENTZONE_PRESENSE
# zone.nrOfZonePoints = 4
# zone.zoneData[0] = ZoneDataPoint(-20.0, 40.0)
# zone.zoneData[1] = ZoneDataPoint(20.0, 40.0)
# zone.zoneData[2] = ZoneDataPoint(20.0, 20.0)
# zone.zoneData[3] = ZoneDataPoint(-20.0, 20.0)

# res = lib.ITR3800_setEventZones(handle, event)
# if res != 0:
#     print("Error – ITR3800_setEventZones failed")
# else:
#     print("Event zone set successfully.")

# time.sleep(1)

# === GET NUMBER OF SET EVENT ZONES ===

# eventzones = ITR3800_EventZones_t()
# res = lib.ITR3800_getEventZones(handle, ctypes.byref(eventzones))

# if res != 0:
#     print("Error – ITR3800_getEventZones failed")
# else:
#     nrOfEventZones = sum(1 for z in eventzones.eventZones if z.enable)
#     print(f"Number of set event zones: {nrOfEventZones}")

# === CLEAR EVENT ZONES ===

# clear_event = ITR3800_EventZones_t()  # Zeroed out struct
# res = lib.ITR3800_setEventZones(handle, clear_event)
# if res != 0:
#     print("Error – ITR3800_setEventZones (clear) failed")
# else:
#     print("Event zones cleared.")

# time.sleep(1)


#-------- def Exit system

# lib.ITR3800_exitSystem.restype = ctypes.c_int
# lib.ITR3800_exitSystem.argtypes = [ctypes.c_void_p]

# exit_res = lib.ITR3800_exitSystem(handle)
# print("Exited successfully" if exit_res == 0 else f"Failed to exit. Code: {exit_res}")
