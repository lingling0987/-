
#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�4��12��
"""

import random



#0 - ʯͷ
#1 - ʷ����
#2 - ֽ
#3 - ����
#4 - ����
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):  # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    """
    ����Ϸ�����Ӧ����ͬ������   
    """
    if name==("ʯͷ"):
     return 0
    elif name==("ʷ����"):
     return 1
    elif name==("ֽ"):
     return 2
    elif name==("����"):
     return 3
    elif name==("����"):
     return 4
    else:
     return -100  # ��Ҫ���Ƿ��ؽ��
    
   


 
   
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
	    return "ֽ"
    elif number==3:
	    return "����"
    elif number==4:
	    return "����"
    

      
  

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    
    comp_number=random.randrange(0,5)                           # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    number_to_name(comp_number)                                 # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    player_choice_number=name_to_number(player_choice)          # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    
    if player_choice_number==comp_number:                       # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
	    print("�������ѡ��Ϊ��",number_to_name(comp_number))      # ����Ļ����ʾ�����ѡ����������
	    print("���ͼ��������һ����")                               # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    elif 0<player_choice_number-comp_number<=2:   
        print("�������ѡ��Ϊ��",number_to_name(comp_number))      # ����Ļ����ʾ�����ѡ����������
        print("��Ӯ��")
    elif -2<=player_choice_number-comp_number<=-1:
        print("�������ѡ��Ϊ��",number_to_name(comp_number))      # ����Ļ����ʾ�����ѡ����������
        print("�����Ӯ��")
    elif player_choice_number-comp_number>=3:
        print("�������ѡ��Ϊ��",number_to_name(comp_number))      # ����Ļ����ʾ�����ѡ����������
        print("�����Ӯ��")
    elif -4<player_choice_number-comp_number<-2:
        print("�������ѡ��Ϊ��",number_to_name(comp_number))      # ����Ļ����ʾ�����ѡ����������
        print("��Ӯ��")
    else:
        print("Error: No Correct Name")
   
player_choice=input("����������ѡ��:")                     # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
print("----------------")                                # ���"-------- "���зָ�
print("����ѡ���ǣ�",player_choice)
rpsls(player_choice)	

   

     


# �Գ�����в���
#print("��ӭʹ��RPSLS��Ϸ")
#print("----------------")
#print("����������ѡ��:")
#choice_name=input()
#rpsls(choice_name)


