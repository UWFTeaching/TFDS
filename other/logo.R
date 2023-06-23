
 p = mtcars %>%
  ggplot(aes(x = mpg, y = wt) , ) + 
  geom_point(aes(col=factor(cyl))) +
  geom_smooth() +
  theme_void() + 
  theme_transparent()+
  theme(legend.position = "none")  

  
  sticker(p, package="Tools+Stat 4DS", p_size=15, s_x=1, s_y=.75, s_width=1.3, s_height=1,dpi = "retina",
          filename="logo.png")


  annotate('text',x = 14,y = 4.5,label="SELECT SQL",col="blue",size=8) +
  annotate('text',x = 20,y = 4,label="> R",col="black",size=8)+
  annotate('text',x = 26,y = 3.5,label=">>> Python",col="red",size=8)+
  annotate('text',x = 26,y = 2.5,label="Statistics",col="brown",size=8)



