class Video:
    def __init__(self, vl, p, os, oe, c):
        self.video_mnt, self.video_sec = int(vl[:2]), int(vl[3:])
        self.pos = p
        self.op_start_mnt, self.op_start_sec =  int(os[:2]), int(os[3:])
        self.op_end_mnt, self.op_end_sec = int(oe[:2]), int(oe[3:])
        self.commands = c
        self.mnt, self.sec = int(p[:2]), int(p[3:])
        self.calCommands()
        
    def isOP(self,curm, curs):
        osflag = 0
        oeflag = 0
        if self.op_start_mnt == curm:
            if curs >= self.op_start_sec:
                osflag = 1
        elif self.op_start_mnt < curm:
            osflag = 1
        
        if self.op_end_mnt == curm:
            if curs <= self.op_end_sec:
                oeflag = 1
        elif self.op_end_mnt > curm:
            oeflag = 1
            
        if osflag == 1 and oeflag == 1:
            return True
        else:
            return False
        
    def isEnd(self,curm, curs):
        if curm == self.video_mnt:
            if curs >= self.video_sec:
                return True
        elif curm > self.video_mnt:
            return True
        return False
        
    def calCommands(self):
        curm, curs = self.mnt, self.sec
        
        if self.isOP(curm,curs):
            curm, curs = self.op_end_mnt, self.op_end_sec
        
        for command in self.commands:
            if command == 'prev':
                if curs - 10 < 0:
                    curs = 50 + curs
                    curm -= 1
                else:
                    curs -= 10
                if curm < 0:
                    curm, curs = 0, 0
                if self.isOP(curm, curs):
                    curm, curs = self.op_end_mnt, self.op_end_sec
                    
            elif command == 'next':
                if curs + 10 >= 60:
                    curs = curs - 50
                    curm += 1
                else:
                    curs += 10
                if self.isOP(curm, curs):
                    curm, curs = self.op_end_mnt, self.op_end_sec
                if self.isEnd(curm, curs):
                    curm, curs = self.video_mnt,self.video_sec 
                    
        self.mnt, self.sec = curm, curs
                
    def getTime(self):
        m, s ='',''
        if self.mnt <10:
            m = '0'+str(self.mnt)
        else:
            m = str(self.mnt)
        if self.sec < 10:
            s = '0'+str(self.sec)
        else:
            s = str(self.sec)
            
        return m,s

def solution(video_len, pos, op_start, op_end, commands):
    video = Video(video_len, pos, op_start, op_end, commands)
    mnt, sec = video.getTime()
    answer = mnt + ':' + sec
    return answer