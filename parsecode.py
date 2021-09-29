import ast,os,re,argparse

def titlecase_text(istr):
	"""this function is unique idea by: Nikhil Swami the great"""
	result=''
	if istr:
		result=re.sub(r'\w+',lambda m:m.group(0)[0].upper()+m.group(0)[1:],istr)

	# result=re.sub(r'\w*',lambda m:[m.group(0).capitalize(),print(m)][0],istr) #DEBUG
	return result

def generate_markdown(filepath,output='./'):
	modulename=os.path.basename(filepath)
	# print(modulename)
	file=open(filepath,'r').read()
	astmodule=ast.parse(file)
	# print(vars(astmodule))
	moduleDocstring=titlecase_text(ast.get_docstring(astmodule,clean=1)).replace('\n',' ')
	print(f"# MODULE: {modulename} \n {moduleDocstring}\n")
	for x in astmodule.body:
		if type(x) in [ast.FunctionDef,ast.ClassDef,ast.Module]:#logic sugar
			docstring=ast.get_docstring(x,clean=1)
			dsmessage=''
			# print(f"\n---")
			try:
				print(vars(x.args.defaults[0]))
			except:
				pass
			print(f'## Function: **{x.name}**({",".join(y.arg for y in x.args.args)})')
			if not docstring:
				dsmessage+='Sorry, Developer Has not provided docstring for this function'
			else:
				dsmessage+="\n".join('- '+x for x in docstring.split('\n'))
			print(dsmessage+'<br><br>\n')

def main():
	if len(sys.argv)>1:
		if os.path.isfile(sys.argv[1]):
			generate_markdown(sys.argv[1])


if __name__ == '__main__':
	main()








UNITTESTS=0
if UNITTESTS:
	titlecase_text('which allows uninterrupted and smart execution of NPC tiles')