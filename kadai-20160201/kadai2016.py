import mcpi.minecraft as minecraft
import mcpi.block as block
import math
#def setup_ground (mc, bid):
#    pos = 0
#    pos = 0
#    mc.setBlocks(pos.x-100,-100, pos.z-100, pos.x+100, pos.y, pos.z+100, block.\
#GRASS)
#    mc.setBlocks(pos.x-100, 1, pos.z-100, pos.x+100, pos.y+100, pos.z+100, bloc\
#k.AIR.id)


def setup_ground2 (mc, bid):
    size = 50
    pos = (0,0,0)
#    pos = 0
    mc.setBlocks(0, 0, 0, size, 0, size, bid)
    mc.setBlocks(1, 0, 1, size-1, 10, size-1, block.AIR.id)

#def setup_ground3 (mc, bid):
#    size = 64
#    pos = (0,0,0)
#    pos = 0
#    ba = 0
#    r = 31

#    for var in range(0, 31400):
#        a = float(var)/100
#        mc.setBlock(32+r*math.cos(a), a, 32+r*math.sin(a), bid)
#        print a
mc = minecraft.Minecraft.create("133.45.175.34")
mc.postToChat("Start: kadai2016")

#setup_ground(mc, block.BRICK_BLOCK.id)
setup_ground2(mc, block.BRICK_BLOCK.id)
#setup_ground3(mc, block.BRICK_BLOCK.id)

mc.postToChat("End: kadai2016")
print "End"
