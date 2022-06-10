package com.func;
import com.pro.Process;
public class HRRN extends Scheduling{
	
	public HRRN(int processorNum) {super(processorNum);}
	// ���ť ���� �ִ� ��� ���μ����� ���ð��� 1�� ���դ��ϴ�.
	public void addWaitTime() {
		for (int i = 0; i < waitQ.size(); i++) waitQ.get(i).addWaitTime();
	}
	// HRRN�˰��� ���ؼ� ���ť�� �ִ� ���μ����� ���� �켱������ ���� ���μ����� �ε����� ��ȯ�մϴ�.
	public int pick() {
		int maxIdx=0;
		double maxVal=0;
		for(int i=0;i<waitQ.size();i++) {
			double ratio;
			ratio = (double)waitQ.get(i).getWaitTime()/waitQ.get(i).getBurTime();
			if(ratio>maxVal) {
				maxIdx=i;
				maxVal=ratio;
			}	
		}
		return maxIdx;
	}
	// ���� �����층
	@Override
	public Process[] doScheduling() {
		int index=0;
		Process[] rePro=new Process[15];
		printProcessInfo();
		for (int time = 0; !isEnd(); time++) {
			setWaitQ(time);
			for(int i=0;i<processorNum;i++) {
				if(checkRemain(time,i)) {
					rePro[index++]=processor[i];
					processor[i]=null;
				}
				if(processor[i]==null) {
					if(!waitQ.isEmpty()) {
						int idx=pick();
						processor[i] = waitQ.get(idx);
						waitQ.remove(idx);
					}	
				}else processor[i].reduRemainTime();
			}
			addWaitTime();
		}
		return rePro;
	}
}