class WindowResolutionState:
    NUMBERS_OF_RESOLUTIONS = 18
    RESOLUTION_320X240   = 320, 240 #0
    RESOLUTION_480X320   = 480, 320 #1
    RESOLUTION_640X480   = 640, 480 #2
    RESOLUTION_800X480   = 800, 480 #3
    RESOLUTION_800X600   = 800, 600 #4
    RESOLUTION_1024X600  = 1024, 600 #5
    RESOLUTION_1024X768  = 1024, 768 #6
    RESOLUTION_1280X720  = 1280, 720 #7
    RESOLUTION_1280X800  = 1280, 800 #8
    RESOLUTION_1280X1024 = 1280, 1024 #9
    RESOLUTION_1366X768  = 1366, 768 #10
    RESOLUTION_1400X1050 = 1400, 1050 #11
    RESOLUTION_1440X900  = 1440, 900 #12
    RESOLUTION_1600X900  = 1600, 900 #13
    RESOLUTION_1600X1024 = 1600, 1024 #14
    RESOLUTION_1600X1200 = 1600, 1200 #15
    RESOLUTION_1680X1050 = 1680, 1050 #16
    RESOLUTION_1920X1080 = 1920, 1080 #17

    @staticmethod
    def get_resolution_from_index(index):
        match index:
            case 0:
                return WindowResolutionState.RESOLUTION_320X240
            case 1:
                return WindowResolutionState.RESOLUTION_480X320
            case 2:
                return WindowResolutionState.RESOLUTION_640X480
            case 3:
                return WindowResolutionState.RESOLUTION_800X480
            case 4:
                return WindowResolutionState.RESOLUTION_800X600
            case 5:
                return WindowResolutionState.RESOLUTION_1024X600
            case 6:
                return WindowResolutionState.RESOLUTION_1024X768
            case 7:
                return WindowResolutionState.RESOLUTION_1280X720
            case 8:
                return WindowResolutionState.RESOLUTION_1280X800
            case 9:
                return WindowResolutionState.RESOLUTION_1280X1024
            case 10:
                return WindowResolutionState.RESOLUTION_1366X768
            case 11:
                return WindowResolutionState.RESOLUTION_1400X1050
            case 12:
                return WindowResolutionState.RESOLUTION_1440X900
            case 13:
                return WindowResolutionState.RESOLUTION_1600X900
            case 14:
                return WindowResolutionState.RESOLUTION_1600X1024
            case 15:
                return WindowResolutionState.RESOLUTION_1600X1200
            case 16:
                return WindowResolutionState.RESOLUTION_1680X1050
            case 17:
                return WindowResolutionState.RESOLUTION_1920X1080
            case _:
                return WindowResolutionState.RESOLUTION_320X240
