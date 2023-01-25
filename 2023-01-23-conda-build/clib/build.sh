
# autogen.sh is needed to regenerate configure
# for arm mac, not needed elsewhere
bash ./autogen.sh

./configure --prefix=$PREFIX --disable-Werror --with-libsodium
make -j${CPU_COUNT:-1}
make install
