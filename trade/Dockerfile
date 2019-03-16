FROM centos
MAINTAINER hjj<18287251710@163.com>
ENV MYPATH /usr
WORKDIR $MYPATH
ADD . /usr/code
RUN yum -y install vim
RUN yum -y install net-tools
 
CMD /bin/bash
