U
    {`�  �                   @   s�  d dl mZ d dlZd dlZd dlZd dlZd dl mZ e�d� e�d� e�d� dZ	e
e	d� d	d
� Ze�d� ed� e�d� ed� e�d� e�d� e�d� e�d� e
e	d� e�d� e
d� zedd�Ze�� Zej W nJ   eed��Zedd�Ze�e� ej edd�Ze�� Zej Y nX z&edd�Zedd�Ze�� Zej W nJ   eed��Zedd�Ze�e� ej edd�Ze�� Zej Y nX eZeZed�Zedee�ZeZdd� Zedk�r�e�  dS )�    )�TelegramClientN)�eventszgit pullg       @�cleara�  [1;32;40m
__________________________________________________________________
[1;31;40m
[1;33;40m _______     ______  ___________                                                           
[1;34;40m|   _   \   /      \(      _    )                                                          
[1;35;40m(. |_)  :) // ____  \)__/  \__/                                                           
[1;35;40m|:     \/ /  /    ) :)  \_ /                                                              
[1;38;40m(|  _  \(: (____/ //   |.  |                                                              
[1;38;40m|: |_)  :)\        /    \:  |                                                              
[1;39;40m(_______/  "_____/      \__|                                                              
                                                                                           
[1;41;40m ___________  _______  ___       _______   _______    _______        __       ___      ___ 
[1;30;40m("     _   ")/"     "||"  |     /"     "| /" _   "|  /"      \      /""\     |"  \    /"  |
[1;31;40m )__/  \__/(: ______)||  |    (: ______)(: ( \___) |:        |    /    \     \   \  //   |
[1;31;40m    \_ /    \/    |  |:  |     \/    |   \/ \      |_____/   )   /' /\  \    /\  \/.    |
[1;43;40m    |.  |    // ___)_  \  |___  // ___)_  //  \ ___  //      /   //  __'  \  |: \.        |
[1;32;40m    \:  |   (:      "|( \_|:  \(:      "|(:   _(  _||:  __   \  /   /  \  \ |.  \    /:  |
[1;31;40m     \__|    \_______) \_______)\_______) \_______) |__|  \___)(___/    \___)|___|\__/|___|
                                                                                           

� c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
g�������?)�sys�stdout�write�flush�time�sleep)�s�c� r   �telegram_bot.py�	slowprint    s    
r   z"[1;96mStarting Telegram..........g      �?z![;93mCreated by shehan Lahiru...�datezA Whaiting Respondzapi.txt�rzPaste Your api here :- �wzhash.txtzPaste hash URL here :- zEnter send message: ZUsernamec                  C   s.   t ��  t �tjdd��dd� �} t ��  d S )NT)Zincomingc                 �   s*   | j r&t�d� t�| jjt�I d H  d S )N�   )Z
is_privater   r   �clientZsend_message�messageZfrom_id)Zeventr   r   r   �_X   s    
zmain.<locals>._)r   �startZonr   Z
NewMessageZrun_until_disconnected)r   r   r   r   �mainT   s    
r   �__main__)Ztelethonr   Zasyncior   r   �osr   �systemr   �name�printr   �open�f�readZapi�close�str�input�wrr	   �hashZapi_idZapi_hashZmassager   r   r   �__name__r   r   r   r   �<module>   sn   























