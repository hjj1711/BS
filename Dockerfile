FROM centos
MAINTAINER hjj<18287251710@163.com>
ENV MYPATH /usr
WORKDIR $MYPATH
ADD . /usr/code
RUN yum -y install vim
RUN yum -y install net-tools
#用于安装python3的依赖
RUN yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
RUN yum install xz gcc zlib zlib-devel wget sqlite-devel openssl-devel -y
#用于安装scrapy的依赖
RUN yum groupinstall -y development tools
RUN yum install -y epel-release libxslt-devel libxml2-devel openssl-devel
 
CMD /bin/bash
