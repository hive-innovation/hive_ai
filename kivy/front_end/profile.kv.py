MDScreen:
    name:"dashboard"
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Button:
            text:"courses"
            size_hint: .66, .065
            pos_hint:{"center_x": .1, "center_y": .7}
            background_color:0, 0, 0, 0
            #font_name:"BPoppins"
            on_release:
             #info show in box below
            canvas.before:
                Color:
                    rgb:rgba(52,0,231,255)
                RoundedRectangle:
                    size: self.size
                    pos:self.pos
                    radius:[6]
        Button:
            text:"completed"
            size_hint: .66, .065
            pos_hint:{"center_x": .1, "center_y": .68}
            background_color:0, 0, 0, 0
            #font_name:"BPoppins"
            color:rgba(52,0,231,255)
            on_release:
                 #info show in box below
            canvas.before:
                Color:
                    rgb:rgba(52,0,231,255)
                Line:
                    width: 1.2
                    rounded_rectangle:self.x,self.y,self.width,self.height,5,5,5,5,100