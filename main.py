a
    ?A"aH  ?                   @   s?  d dl mZmZ d dlmZ d dlmZ d dlZd dl	Z	d dl
Zd dlZd dlZd dlZd dlZd dlZde	j	_z
e? ZW nT ey?   ze?  e? ZW n0 ey?   edd? edd	? e?d ? Y n0 Y n0 d
Zdd? Zdd? Zdd? ZdZdZdZdZdZdZeddd? ?z?e? e?Z!e"de? de? de? de? ?dd? e!ek?r\e!Ze?r\e Ze? d??r?dZzeed??ZdZW n e#?y?   dZY ?qY n0 e? d ??r?d!Zzeed"??ZdZW n e#?y?   dZY ?qY n0 e? ?r?e?r?zte$e%ee ??D ]ZZ&e?'de(ee e& d  ed#  ?e(ee e& d ed#  ?? e?)ee e& d! ? ?qdZW n e*?y?   dZY ?qY n0 e? d$??r?edd? edd	? e?d ? e?)d%? ?qW n2 e?y?   edd? edd	? e?d ? Y n0 dS )&?    )?config_generator?read_config)?recoil_patterns)?print_bannerNz/C:\\Program Files\\Tesseract-OCR\\tesseract.exeZsinglezheader-stopzno-clearzaction-close-program?deletec                 C   s?   | dkrTt jtd d td d td d td d fd?}t?t?|?tj?}|S | dkr?t jtd	 d td	 d td	 d td	 d fd?}t?t?|?tj?}|S td
? td| ? ?? t	?
d? d S )N?oneZscan_coord_one?left?top?widthZheight)Zregion?twoZscan_coord_twoz9ERROR: Invalid weapon selection | FUNC: weapon_screenshotzVALUE: select_weapon = ?   )?	pyautoguiZ
screenshot?data?cvZcvtColor?npZarrayZCOLOR_RGB2BGR?print?sys?exit)Zselect_weaponZimage? r   ?main.py?weapon_screenshot   s    44r   c                 C   s   t ?| ?}|?? }t|d ?S )Nr   )?pytesseractZimage_to_string?split?str)Zcv_image?textr   r   r   ?read_weapon*   s    
r   c                  C   s   t ?d?} | dk S )Nr   r   )?win32apiZGetKeyState)Z
left_clickr   r   r   ?left_click_state/   s    
r   Fr   ?NoneZdoublezheader-startzuser-optionszRECOIL-CONTROL: z | ACTIVE-WEAPON: z | RECOGNIZED: z | SUPPORTED: z )?end?1r   T?2?   r   Zmodifier_value?/g????MbP?)+Zmodules.helpersr   r   Zmodules.recoil_patternsr   Zmodules.bannersr   Znumpyr   r   Zcv2r   r   Zkeyboardr   ?timer   Ztesseract_cmdr   ?FileNotFoundError?KeyboardInterruptr   Ztoggle_buttonr   r   r   Zactive_stateZlast_toggle_stateZactive_weapon_slotZactive_weaponZsupported_weaponZrecognized_weaponZ
is_pressedZ	key_stater   ?
IndexError?range?len?iZmouse_event?int?sleep?KeyErrorr   r   r   r   ?<module>   s?   




$
>




