<%@page contentType="text/html; charset=UTF-8"%>
<%@page import="Cookie.cookie" %>
<%
	cookie c = new cookie();
	String uname = c.returnName();
	String uid =  c.returnID(); 
%>