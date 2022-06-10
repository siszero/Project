package com.func;

import com.pro.Process;

public class SRTN extends Scheduling {
	public SRTN(int processorNum) {
		super(processorNum);
	}
	@Override
	public Process[] doScheduling() {         
        int index=0;
        Process[] rePro = new Process[15];
        printProcessInfo();   //���μ��� ���� ���. ������
        for (int time = 0; !isEnd(); time++) {
           setWaitQ(time);   //�� �ð��������� ������ ���μ����� ���ť�� �־��ݴϴ�.
           System.out.println("QS "+waitQ.size());
           for(int i=0;i<processorNum;i++) {   //���μ����� ������ŭ �ݺ�
              if(checkRemain(time,i)) {      //���μ����� �������� �˻��մϴ�.
                 rePro[index++]=processor[i];
                 processor[i] = null;
              }
              if(processor[i]==null) {     
                    if(!waitQ.isEmpty())   {  
                       processor[i] = waitQ.get(findNext());  
                       waitQ.remove(findNext());       
                    }
                 }
              else if (!waitQ.isEmpty() && (processor[i].getRemainTime() > waitQ.get(findNext()).getRemainTime())) {
                 processor[i].reduRemainTime();
                 if (processor[i].getRemainTime() >1) {
                    waitQ.add(processor[i]);                 
                 }
                 processor[i] = waitQ.get(findNext());
                 waitQ.remove(findNext());
              }
              else {
                 processor[i].reduRemainTime();
              }
           }
        }
        return rePro;
     }
  public int findNext() {               
     int min = Integer.MAX_VALUE;
     int index = 0;
     for(int i = 0; i < waitQ.size(); i++) {
        if(waitQ.get(i).getRemainTime() < min ) {
           min = waitQ.get(i).getRemainTime();
           index = i;
        }
     }
     return index;
  } 
}