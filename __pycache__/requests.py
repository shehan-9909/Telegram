U
    m�`3  �                   @   sN   d dl mZ d dlZd dlZd dlZd dlZdZe�e� dZdZ	dd� Z
dS )�    )�ClientN�   zI used telegramz+94774593440c                  C   sD   t �d� ttd� t} t}t}t}t||�}|jjdt	t
d�}d S )N�clear�
zwhatsapp:+14155238886)Zfrom_�body�to)�os�system�print�nameZsid�tokenr   �messages�create�t�sr)Z	irc_inputZ
irc_joinigZprint_inputZprint_output�client�message� r   �5/data/data/com.termux/files/home/Telegram/requests.py�setup   s    


�r   )Ztwilio.restr   �sysr   �time�socket�timeout�setdefaulttimeoutr   r   r   r   r   r   r   �<module>   s   
