from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField  # 各类验证
from wtforms.validators import DataRequired  # 验证器


class PostForm(FlaskForm):
    username = StringField('姓名', validators=[DataRequired(message='学号！')],
                           render_kw={'placeholder': '请输入姓名'})
    student_id = StringField('学号', validators=[DataRequired(message='姓名！')],
                             render_kw={'placeholder': '请输入学号'})
    submit = SubmitField('提交')
