library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;


entity program_memory is
    generic (
        ADDRESS_WIDTH: natural := 6;
        DATA_WIDTH: natural := 32
    );
    
    port (
        clk: in std_logic;
        write_en: in std_logic;
        write_data: in std_logic_vector(DATA_WIDTH-1 downto 0);
        address: in std_logic_vector(ADDRESS_WIDTH-1 downto 0);
        read_data : out std_logic_vector(DATA_WIDTH-1 downto 0)
    );
end program_memory;

architecture behavioral of program_memory is

    constant MEMORY_DEPTH: natural := 2 ** ADDRESS_WIDTH;

    type ram_type is array (0 to MEMORY_DEPTH-1) of std_logic_vector(7 downto 0);
    signal read_byte : std_logic_vector(7 downto 0);

    
    impure function initRAM(filename: in string) return ram_type is
        FILE ram_file: text open read_mode is filename;
        variable ram_file_line: line;
        variable instruction: bit_vector(DATA_WIDTH-1 downto 0);
        variable instruction_c: bit_vector(DATA_WIDTH/2-1 downto 0);
        variable ram: ram_type := (others => (others => '0'));
        variable i : integer;
         
    begin
        i := 0;
        for j in 0 to MEMORY_DEPTH/4 loop
            if(not endfile(ram_file)) then
                readline(ram_file, ram_file_line);
                --initalizing with LSB at the smaller address so we can test its opcode for compressed/non-compressed                 
                if ram_file_line'length = 16 then
                    read(ram_file_line, instruction_c);
                    ram(i+1)   := to_stdlogicvector((instruction_c(15 downto  8)));
                    ram(i)     := to_stdlogicvector((instruction_c( 7 downto  0)));
                    i := i +2;
                else 
                    read(ram_file_line, instruction);
                    ram(i+3) := to_stdlogicvector((instruction(31 downto 24)));
                    ram(i+2) := to_stdlogicvector((instruction(23 downto 16)));
                    ram(i+1) := to_stdlogicvector((instruction(15 downto  8)));
                    ram(i)   := to_stdlogicvector((instruction( 7 downto  0)));
                    i := i+4;
                end if; 
                
                          
            end if;
        end loop;        
        return ram;        
    end function;
    
    signal ram: ram_type := initRAM("branch_bin.mem");
    -- word addresable
    alias word_address: std_logic_vector(ADDRESS_WIDTH-2 downto 0) is address(ADDRESS_WIDTH-1 downto 1);

begin

    instruction_ram: process (clk) is
    begin
        if rising_edge(clk) then
            if write_en = '1' then
            -- we re only writing on multiples of 2 to keep the alignment and 32 bit values
                ram(to_integer(unsigned(word_address)&'0'))     <= write_data(31 downto 24);
                ram(to_integer(unsigned(word_address)&'0'+1))       <= write_data(23 downto 16);
                ram(to_integer(unsigned(word_address)&'0'+2))       <= write_data(15 downto  8);
                ram(to_integer(unsigned(word_address)&'0'+3))       <= write_data( 7 downto  0);
                
            end if;
        end if;
    end process instruction_ram;
--if ram data is compressed then read instrc & 000 else read instrs(i) & instrc(i+1)
    read_byte <= ram(to_integer(unsigned(word_address)&'0'));

    reading_ram : process (word_address, read_byte) is
        begin
        --again reading only from addresses that are multiple of 2
            if read_byte(1 downto 0) = "11" then
            --normal instr
            read_data( 7 downto  0) <= ram(to_integer(unsigned(word_address)&'0'));
            read_data(15 downto  8) <= ram(to_integer(unsigned(word_address)&'0')+1);
            read_data(23 downto 16) <= ram(to_integer(unsigned(word_address)&'0')+2);
            read_data(31 downto 24) <= ram(to_integer(unsigned(word_address)&'0')+3);
            else
            read_data( 7 downto  0) <= ram(to_integer(unsigned(word_address)&'0'));
            read_data(15 downto  8) <= ram(to_integer(unsigned(word_address)&'0')+1);
            read_data(23 downto 16) <= (others => '0');
            read_data(31 downto 24) <= (others => '0');
            end if;

        
        end process reading_ram;

end behavioral;