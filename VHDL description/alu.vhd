library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity alu is
    generic(DATA_WIDTH: integer := 32);

    port(
        control: in std_logic_vector(3 downto 0);
        left_operand: in std_logic_vector(DATA_WIDTH-1 downto 0);
        right_operand: in std_logic_vector(DATA_WIDTH-1 downto 0);
        zero: out std_logic;
        result: out std_logic_vector(DATA_WIDTH-1 downto 0)
    );
end alu;

architecture behavioral of alu is

    signal alu_result, sub: std_logic_vector(DATA_WIDTH-1 downto 0);
    constant zeros: std_logic_vector(DATA_WIDTH-2 downto 0):= (others => '0');

begin

    process(control, left_operand, right_operand)
    begin
    

        case control is
            when "0000" => 
                alu_result <= left_operand and right_operand;
            when "0001" => 
                alu_result <= left_operand or right_operand;
            when "0010" =>
                alu_result <= std_logic_vector(signed(left_operand) + signed(right_operand));
            when "0011" => 
                alu_result <= left_operand xor right_operand;
            when "0110" => 
                alu_result <= std_logic_vector(signed(left_operand) - signed(right_operand));
                --SLL
            when "0111" => 
                alu_result <= std_logic_vector(shift_left(unsigned(left_operand),to_integer(unsigned(right_operand))));
                --SRL
            when "0100" => 
                alu_result <= std_logic_vector(shift_right(unsigned(left_operand),to_integer(unsigned(right_operand))));
                --SRA
            when "0101" => 
                    alu_result <= std_logic_vector(shift_right(signed(left_operand),to_integer(unsigned(right_operand))));   
                 --SLT
            when "1000" => 
                    if signed(left_operand) < signed(right_operand) then
                        alu_result <= zeros & '1';
                    else 
                        alu_result <= zeros & '0';   
                    end if;
                 --SLTU   
            when "1001" => 
                    if unsigned(left_operand) < unsigned(right_operand) then
                        alu_result <= zeros & '1';
                    else 
                        alu_result <= zeros & '0';   
                    end if;                                                
            when others => 
                alu_result <= left_operand and right_operand;
        end case;
    end process;

    result <= alu_result;
    zero <= '1' when signed(alu_result) = 0 else '0';

end behavioral;