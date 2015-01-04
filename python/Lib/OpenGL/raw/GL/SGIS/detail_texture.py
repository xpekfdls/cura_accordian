'''OpenGL extension SGIS.detail_texture

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_detail_texture'
_DEPRECATED = False
GL_DETAIL_TEXTURE_2D_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_2D_SGIS', 0x8095 )
GL_DETAIL_TEXTURE_2D_BINDING_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_2D_BINDING_SGIS', 0x8096 )
GL_LINEAR_DETAIL_SGIS = constant.Constant( 'GL_LINEAR_DETAIL_SGIS', 0x8097 )
GL_LINEAR_DETAIL_ALPHA_SGIS = constant.Constant( 'GL_LINEAR_DETAIL_ALPHA_SGIS', 0x8098 )
GL_LINEAR_DETAIL_COLOR_SGIS = constant.Constant( 'GL_LINEAR_DETAIL_COLOR_SGIS', 0x8099 )
GL_DETAIL_TEXTURE_LEVEL_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_LEVEL_SGIS', 0x809A )
GL_DETAIL_TEXTURE_MODE_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_MODE_SGIS', 0x809B )
GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS = constant.Constant( 'GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS', 0x809C )
glDetailTexFuncSGIS = platform.createExtensionFunction( 
'glDetailTexFuncSGIS',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,arrays.GLfloatArray,),
doc='glDetailTexFuncSGIS(GLenum(target), GLsizei(n), GLfloatArray(points)) -> None',
argNames=('target','n','points',),
deprecated=_DEPRECATED,
)

glGetDetailTexFuncSGIS = platform.createExtensionFunction( 
'glGetDetailTexFuncSGIS',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,arrays.GLfloatArray,),
doc='glGetDetailTexFuncSGIS(GLenum(target), GLfloatArray(points)) -> None',
argNames=('target','points',),
deprecated=_DEPRECATED,
)


def glInitDetailTextureSGIS():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
