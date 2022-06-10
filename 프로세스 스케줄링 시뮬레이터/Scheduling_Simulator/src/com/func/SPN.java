package com.func;
import com.pro.Process;
public class SPN extends Scheduling {
	public SPN(int processorNum) {
		super(processorNum);
	}
	 @Override
	   public Process[] doScheduling() {
	      int index=0;
	      int spn_idx=0;//spn �����ٸ����� �켱������ ���ϱ� ���� �ε���
	      Process[] rePro = new Process[15];
	      printProcessInfo();   //���μ��� ���� ���. ������
	      for (int time = 0; !isEnd(); time++) {
	         setWaitQ(time);   //�� �ð��������� ������ ���μ����� ���ť�� �־��ݴϴ�.
	         int min = Integer.MAX_VALUE;
	         //time�� ���������� burst_time�� ���� ���� ���μ����� �ε����� ã�Ƽ� �������ش�.
	         for(int i = 0; i < waitQ.size(); i++) {
	            if(waitQ.get(i).getBurTime() < min) {
	               min = waitQ.get(i).getBurTime();
	               spn_idx = i;
	            }
	         }
	         //System.out.println("time : "+time+"Index : "+index+"size : "+waitQ.size());
	         for(int i=0;i<processorNum;i++) {   //���μ����� ������ŭ �ݺ�
	            if(checkRemain(time,i)) {      //���μ����� �������� �˻��մϴ�.
	               rePro[index++]=processor[i];
	               processor[i] = null;
	               }
	            if(processor[i]==null) {      //���μ����� ����������
	               if(!waitQ.isEmpty()) {      //�׸��� ���ť�� ���μ����� �ִ°��
	                  processor[i] = waitQ.get(spn_idx);   //���ť���� bur_time�� ���� ���� ���μ����� �����ɴϴ�.
	                  waitQ.remove(spn_idx);//������ ť�� �����մϴ�.
	                  }
	               }
	            else processor[i].reduRemainTime();   //���μ����� ���ǰ������� remain time�� ���ҽ�ŵ�ϴ�.
	         }
	      }
	      return rePro;
	   }
}
