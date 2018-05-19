import os, subprocess, shutil

import toolspath
from testing import Test, BuildTest

call_fs = "xcheck"

def readall(filename):
  f = open(filename, 'r')
  s = f.read()
  f.close()
  return s


class FSBuildTest(BuildTest):
  targets = [call_fs]
  def run(self):
	self.run_util(['rm','-f',call_fs]);
	status = self.run_util(['gcc', call_fs + '.c', '-o', call_fs, '-Wall', '-Werror', '-O'])
	if status != 0:
	  self.clean([call_fs, '*.o'])
	  #if not self.make(self.targets):
	  self.make(self.targets)
	self.done()
	

class FSTest(Test):
  def run(self, command = None, stderr = None, 
		  addl_args = []):
	filename = self.name
	if self.name == 'valgrind':
		filename = 'mrkused'
	elif self.name == 'valgrind2':
		filename = 'imrkused'
	elif self.name == 'valgrind3':
		filename = 'goodrefcnt'
	in_path = self.test_path + '/images/' + filename
	err_path = self.test_path + '/err/' + filename
	if stderr == None:
		stderr = readall(err_path)
		
	if self.name == 'noimage':
		in_path = ''
		command = ['./' + call_fs]
		self.command = call_fs + \
			"\n and check out the test folder\n " + self.test_path \
			+ '/err/' + self.name + \
			"\n to compare your error output with reference outputs. "

		self.runexe(command, status=self.status, stderr=stderr)
		self.done()
	elif self.name.startswith('valgrind'):
		vgname = "vg_summary.xml"
		vgfile = self.project_path + "/" + vgname
		
		child = self.runexe(["/usr/bin/valgrind", "--show-reachable=yes",
							 "--xml=yes", "--child-silent-after-fork=yes", "--undef-value-errors=no",
							 "--xml-file=" + vgfile, self.project_path + "/./" + call_fs, in_path],stderr=stderr)
		import xml.etree.ElementTree
		summary = xml.etree.ElementTree.parse(vgfile).getroot()
		if summary.find('error') != None:
			shutil.copy2(vgfile, vgname)
			self.fail("Valgrind error, check error section of summary: {0}\n".format(vgname))
		self.done();
	elif self.name == 'repair':
		shutil.copyfile(in_path,self.project_path + "/" + self.name)
		in_path = self.project_path + "/" + self.name
		command = ['./' + call_fs,'-r',in_path]
		self.runexe(command)
		child = subprocess.Popen([self.test_path + "/util/repair_check",in_path], stdout=subprocess.PIPE)
		out = child.communicate()[0]
		if 'PASSED' not in out:
			self.fail("image is not correctly repaired.")
		else:
			self.runexe(['./' + call_fs,in_path], status=self.status, stderr=stderr)
		subprocess.call(['rm','-f',in_path])
		self.done()
		
	else:        
		if command == None:
			command = ['./' + call_fs, in_path]

		self.command = call_fs + " " + in_path + \
			"\n and check out the test folder\n " + self.test_path \
			+ '/err/' + self.name + \
			"\n to compare your error output with reference outputs. "

		self.runexe(command, status=self.status, stderr=stderr)
		self.done()

######################### Built-in Commands #########################

class Noimage(FSTest):
  name = 'noimage'
  description = 'Run without a file system'
  timeout = 10
  status = 1
  point_value = 5

class Good(FSTest):
  name = 'good'
  description = 'Run on a good file system'
  timeout = 10
  status = 0
  point_value = 5

class Nonexistant(FSTest):
  name = 'nonexistant'
  description = 'Run on a nonexistant file system'
  timout = 10
  status = 1
  point_value = 5

class Badinode(FSTest):
  name = 'badinode'
  description = 'Run on a file system with a bad type in an inode'
  timout = 10
  status = 1
  point_value = 5

class Badaddr(FSTest):
  name = 'badaddr'
  description = 'Run on a file system with a bad direct address in an inode'
  timout = 10
  status = 1
  point_value = 5

class Badindir1(FSTest):
  name = 'badindir1'
  description = 'Run on a file system with a bad indirect address in an inode'
  timout = 10
  status = 1
  point_value = 5

class Badindir2(FSTest):
  name = 'badindir2'
  description = 'Run on a file system with a bad indirect address in an inode'
  timout = 10
  status = 1
  point_value = 5

class Badroot(FSTest):
  name = 'badroot'
  description = 'Run on a file system with a root directory in bad location'
  timout = 10
  status = 1
  point_value = 5

class Badroot2(FSTest):
  name = 'badroot2'
  description = 'Run on a file system with a bad root directory in good location'
  timout = 10
  status = 1
  point_value = 5

class Badfmt(FSTest):
  name = 'badfmt'
  description = 'Run on a file system without . or .. directories'
  timout = 10
  status = 1
  point_value = 5

class Mrkfree(FSTest):
  name = 'mrkfree'
  description = 'Run on a file system with an inuse direct block marked free'
  timout = 10
  status = 1
  point_value = 5

class Mrkfreeindir(FSTest):
  name = 'indirfree'
  description = 'Run on a file system with an inuse indirect block marked free'
  timout = 10
  status = 1
  point_value = 5

class Mrkused(FSTest):
  name = 'mrkused'
  description = 'Run on a file system with a free block marked used'
  timout = 10
  status = 1
  point_value = 5

class Addronce(FSTest):
  name = 'addronce'
  description = 'Run on a file system with a direct address used more than once'
  timout = 10
  status = 1
  point_value = 5

class Addronce2(FSTest):
  name = 'addronce2'
  description = 'Run on a file system with an indirect address used more than once'
  timout = 10
  status = 1
  point_value = 5

class Imrkused(FSTest):
  name = 'imrkused'
  description = 'Run on a file system with inode marked used, but not referenced in a directory'
  timout = 10
  status = 1
  point_value = 5

class Imrkfree(FSTest):
  name = 'imrkfree'
  description = 'Run on a file system with inode marked free, but referenced in a directory'
  timout = 10
  status = 1
  point_value = 5

class Badrefcnt(FSTest):
  name = 'badrefcnt'
  description = 'Run on a file system which has an inode that is referenced less than its reference count'
  timout = 10
  status = 1
  point_value = 5

class Badrefcnt2(FSTest):
  name = 'badrefcnt2'
  description = 'Run on a file system which has an inode that is referenced more than its reference count'
  timout = 10
  status = 1
  point_value = 5

class Goodlarge(FSTest):
  name = 'goodlarge'
  description = 'Run on large good file system'
  timout = 10
  status = 0
  point_value = 5

class Goodrefcnt(FSTest):
  name = 'goodrefcnt'
  description = 'Run on a file system with only good file reference counts'
  timout = 10
  status = 0
  point_value = 5

class Goodlink(FSTest):
  name = 'goodlink'
  description = 'Run on a file system with only good directory link counts'
  timout = 10
  status = 0
  point_value = 5
  
class Goodrm(FSTest):
  name = 'goodrm'
  description = 'Run on a good file system having some files removed'
  timout = 10
  status = 0
  point_value = 5

class Dironce(FSTest):
  name = 'dironce'
  description = 'Run on a file system with a directory appearing more than once'
  timout = 10
  status = 1
  point_value = 5

class Badlarge(FSTest):
  name = 'badlarge'
  description = 'Run on a large file system with an indirect directory appearing more than once'
  timout = 10
  status = 1
  point_value = 5

class Valgrind(FSTest):
  name = 'valgrind'
  description = 'Run valgrind on xcheck'
  timout = 10
  status = 1
  point_value = 5

class Valgrind2(FSTest):
  name = 'valgrind2'
  description = 'Run valgrind on xcheck'
  timout = 10
  status = 1
  point_value = 5

class Valgrind3(FSTest):
  name = 'valgrind3'
  description = 'Run valgrind on xcheck'
  timout = 10
  status = 1
  point_value = 5

class Mismatch(FSTest):
  name = 'mismatch'
  description = 'Run on a filesystem with .. pointing to the wrong directory'
  timeout = 5
  status = 1
  point_value = 0

class Loop(FSTest):
  name = 'loop'
  description = 'Run on a filesystem with a loop in the directory tree'
  timeout = 5
  status = 1
  point_value = 0
  
class Repair(FSTest):
  name = 'repair'
  description = 'Repair a filesystem with lost inodes, check if every lost inode is found'
  timeout = 10
  status = 0
  point_value = 0
  
#=========================================================================

all_tests = [
  # Easy tests
  #Noimage,
  Good,
  Goodlarge,
  Goodrefcnt,
  Goodlink,
  Goodrm,
  Nonexistant,
  Badroot,

  # Medium/hard tests
  Badinode,
  Badaddr,
  Badindir1,
  Badroot2,
  Badfmt,
  Mrkfree,
  Mrkfreeindir,
  Mrkused,
  Addronce,
  Addronce2,
  Imrkused,
  Imrkfree,
  Badrefcnt,
  Badrefcnt2,
  Badindir2,
  Dironce,
  Badlarge,
  Valgrind,
  Valgrind2,
  Valgrind3,
  
  # Contest tests
  Mismatch,
  Loop,
  Repair
  ]

build_test = FSBuildTest

from testing.runtests import main
main(build_test, all_tests)
#main(all_tests)
